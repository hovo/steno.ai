import uuid
from pydub import AudioSegment
from google.cloud import storage, speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.protobuf.json_format import MessageToJson
from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
from store import get_file_metadata
import json

GCS_BUCKET_NAME = "steno"
BASE_GCS_URI = "gs://steno/"
#BASE_GCS_URI = "https://storage.googleapis.com/steno/"

def get_metadata(file):
    """
    Returns an object containing the sampling rate and the duration
    """
    af = AudioSegment.from_file(file, format="wav")
    metadata = {
        "file_name": file.filename,
        "sampling_rate": af.frame_rate,
        "channels": af.channels,
        "duration": af.duration_seconds
    }
    return metadata

def upload_to_gcs(file):
    """
    Uploads file to Google Cloud Storage

    Returns
    -------
    string
        Google Cloud Storage URI
    """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(GCS_BUCKET_NAME)

    # Generate an UUID for the filename
    id = str(uuid.uuid4())
    file_type = file.filename.split(".")[-1]
    file_name = "{}.{}".format(id, file_type)

    blob = bucket.blob(file_name)
    blob.upload_from_file(file)

    gcs_uri = BASE_GCS_URI + file_name

    return gcs_uri

def async_transcribe(id):
    """
    Transcribe the given audio file asynchronously and output the word time
    offsets.
    """
    file_metadata = json.loads(get_file_metadata(id))
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=file_metadata['uri'])
    config = types.RecognitionConfig(
        sample_rate_hertz=file_metadata['sampling_rate'],
        enable_word_time_offsets=True,
        enable_automatic_punctuation=True,
        audio_channel_count=file_metadata['channels'],
        language_code='en-US')

    operation = client.long_running_recognize(config, audio)
    return MessageToJson(operation.operation)

def poll_operation(name):
    """
    Polls the status of the long running operation
    """
    credentials = GoogleCredentials.get_application_default()
    speech_service = discovery.build('speech', 'v1', credentials=credentials)

    get_operation_request = speech_service.operations().get(name=name)
    response = get_operation_request.execute()

    if('done' in response):
        return response['response']
    return {"name": response['name']}