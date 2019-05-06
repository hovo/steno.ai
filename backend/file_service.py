from google.cloud import storage
import uuid

GCS_BUCKET_NAME = "steno"

def upload_to_gcs(file):
    '''
    Uploads file to Google Cloud Storage
    '''
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(GCS_BUCKET_NAME)

    # Generate an UUID for the filename
    filename = str(uuid.uuid4()) + "." + file.filename.split(".")[-1]
    blob = bucket.blob(filename)
    blob.upload_from_file(file)