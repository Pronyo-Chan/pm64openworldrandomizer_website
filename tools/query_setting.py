import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Get the count of seeds for a specific setting.
# Requires you to have the service_account.json DB key in the parent folder
# Usage: Edit setting_name and setting_value to desired name and value, then run >python query_setting.py
def main():
    setting_name = 'AlwaysSpeedySpin'
    setting_value = False
    cred = credentials.Certificate('../service_account.json')
    firestore_seeds_collection = "seeds-prod"
    
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    docs = db.collection(firestore_seeds_collection).where(setting_name, '==', setting_value).stream()
    count = 0
    for doc in docs:
        count +=1

    print(f'{count} entries found for setting with name: {setting_name} and value: {setting_value}.')

if __name__ == "__main__":
    main()