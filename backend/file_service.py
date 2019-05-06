from pydub import AudioSegment
from google.cloud import storage
import uuid

GCS_BUCKET_NAME = "steno"

def get_sampling_rate(file):
    """
    Returns the sampling rate for the audio file
    """
    sampling_rate = AudioSegment.from_file(file, format="wav").frame_rate
    return sampling_rate

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
    filename = str(uuid.uuid4()) + "." + file.filename.split(".")[-1]
    blob = bucket.blob(filename)
    blob.upload_from_file(file)

    return filename