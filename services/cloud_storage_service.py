import io
import os
from google.cloud import storage
import services.local_storage as local_storage

from copy import deepcopy

def save_file_to_cloud(filename, file):
    if local_storage.use_local_storage:
        local_storage.local_files[filename] = file
        return

    if not os.path.isfile('service_account.json'):
        raise ConnectionRefusedError(f'service_account.json key was not found, unable to access google cloud storage to save {filename}')

    storage_client = storage.Client.from_service_account_json('service_account.json')

    bucket = storage_client.bucket('paper-mario-randomizer-server.appspot.com')

    blob = storage.Blob(filename, bucket)
    blob.upload_from_file(file)


def get_file_from_cloud(filename):
    if local_storage.use_local_storage:
        file = local_storage.local_files.get(filename)
        if isinstance(file, io.StringIO):
            return io.BytesIO(file.getvalue().encode())
        
        file.seek(0)
        return deepcopy(file)

    if not os.path.isfile('service_account.json'):
        raise ConnectionRefusedError(f'service_account.json key was not found, unable to access google cloud storage to get {filename}')

    storage_client = storage.Client.from_service_account_json('service_account.json')
    bucket = storage_client.get_bucket('paper-mario-randomizer-server.appspot.com')

    blob = bucket.get_blob(filename)
    if blob is None:
        return None
    return io.BytesIO(blob.download_as_bytes())