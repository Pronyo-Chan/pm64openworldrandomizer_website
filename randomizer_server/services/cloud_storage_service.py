import io
import os
from google.cloud import storage

def save_file_to_cloud(filename, file):
    if not os.path.isfile('service_account.json'):
        raise ConnectionRefusedError(f'service_account.json key was not found, unable to access google cloud storage to save {filename}')

    storage_client = storage.Client.from_service_account_json('service_account.json')

    bucket = storage_client.get_bucket('paper-mario-randomizer-server.appspot.com')

    blob = storage.Blob(filename, bucket)
    blob.upload_from_file(file)

    file.seek(0) #Important to reset the file or else the API will return an empty file

def get_file_from_cloud(filename):
    if not os.path.isfile('service_account.json'):
        raise ConnectionRefusedError(f'service_account.json key was not found, unable to access google cloud storage to get {filename}')

    storage_client = storage.Client.from_service_account_json('service_account.json')

    bucket = storage_client.get_bucket('paper-mario-randomizer-server.appspot.com')

    blob = bucket.get_blob(filename)
    if blob is None:
        return None
    return io.BytesIO(blob.download_as_bytes())