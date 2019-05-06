import uuid
from pydub import AudioSegment
from google.cloud import storage, speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.protobuf.json_format import MessageToJson

GCS_BUCKET_NAME = "steno"
BASE_GCS_URI = "https://storage.googleapis.com/steno/"

def audio_file_details(file):
    """
    Returns an object containing the sampling rate and the duration
    """
    af = AudioSegment.from_file(file, format="wav")
    metadata = {
        "file_name": file.filename,
        "sampling_rate": af.frame_rate,
        "duration": af.duration_seconds
    }

    return metadata

def upload_to_gcs(file):
    """
    Uploads file to Google Cloud Storage

    Returns
    -------
    string
        Uploaded file name
    """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(GCS_BUCKET_NAME)

    # Generate an UUID for the filename
    file_name = str(uuid.uuid4()) + "." + file.filename.split(".")[-1]
    blob = bucket.blob(file_name)
    blob.upload_from_file(file)

    gcs_uri = BASE_GCS_URI + file_name

    return gcs_uri

def async_transcribe(gcs_uri, sampling_rate):
    """
    Transcribe the given audio file asynchronously and output the word time
    offsets.
    """
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        enable_word_time_offsets=True,
        sample_rate_hertz=sampling_rate,
        language_code='en-US')
    
    operation = client.long_running_recognize(config, audio)
    response = operation.result(timeout=90)

    return MessageToJson(response)

