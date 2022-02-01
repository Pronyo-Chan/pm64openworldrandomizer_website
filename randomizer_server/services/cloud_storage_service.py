import os
from google.cloud import storage

def save_file_to_cloud(filename, file):
    if not os.path.isfile('service_account.json'):
        return

    storage_client = storage.Client.from_service_account_json('service_account.json')

    bucket = storage_client.get_bucket('paper-mario-randomizer-server.appspot.com')

    blob = storage.Blob(filename, bucket)
    blob.upload_from_file(file)

    file.seek(0) #Important to reset the file or else the API will return an empty file
