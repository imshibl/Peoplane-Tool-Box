import datetime
import os
from io import BytesIO

import firebase_admin
import pandas as pd
from firebase_admin import credentials, db, firestore, storage


class FirebaseHelper:
    # __cred = credentials.Certificate(
    #     "C:\\Users\\bil\\Desktop\\Peoplane Tool Box\\firebase_creds.json"
    # )
    # __firebase_app = firebase_admin.initialize_app(
    #     __cred,
    #     {
    #         "databaseURL": "https://sop-quality-checker-default-rtdb.asia-southeast1.firebasedatabase.app",
    #         "storageBucket": "sop-quality-checker.appspot.com",
    #     },
    # )

    # USE THIS FOR PRODUCTION

    __cred = credentials.Certificate("/etc/secrets/firebase_creds.json")
    firebase_admin.initialize_app(
        __cred,
        {
            "databaseURL": os.getenv("DATABASE_URL"),
            "storageBucket": os.getenv("STORAGE_BUCKET"),
        },
    )

    firestore_db = firestore.client()

    users_ref = firestore_db.collection("Users")
    consultants_ref = firestore_db.collection("Consultants")

    feedbacks_ref = firestore_db.collection("Feedbacks")

    cv_collections_ref = firestore_db.collection("CV_Collections")

    sop_dataset_ref = firestore_db.collection("SOP_Dataset").document("SOP_Dataset")

    maintenance_ref = db.reference("/is_under_maintenance")
    quality_checks_performed_ref = db.reference("/quality_checks_performed")
    plagiarism_checks_performed_ref = db.reference("/plagiarism_checks_performed")
    resume_checks_performed_ref = db.reference("/resume_checks_performed")

    storage_bucket = storage.bucket()

    # PLAGIARISM CHECKER
    @classmethod
    def download_csv_as_df(cls, blob_path):
        blob = cls.storage_bucket.blob(blob_path)
        csv_content = blob.download_as_bytes()
        df = pd.read_csv(BytesIO(csv_content))

        return df

    @classmethod
    def upload_df_as_csv(cls, df, blob_path):
        blob = cls.storage_bucket.blob(blob_path)

        blob.upload_from_string(df.to_csv(index=False), content_type="text/csv")

        url = blob.generate_signed_url(
            expiration=datetime.timedelta(days=365), method="GET"
        )
        print(url)

        current_datetime = datetime.datetime.utcnow().strftime("%d-%m-%Y")
        data = {
            "download_url": url,
            "last_updated": current_datetime,
        }
        cls.sop_dataset_ref.set(data)

    # RESUME ANALYZER
    @classmethod
    def upload_cv_to_storage(cls, file, destination_filename, content_type):
        # Create a blob (object) in the bucket
        blob = cls.storage_bucket.blob(destination_filename)

        # Seek to the beginning of the file stream
        file.seek(0)

        # Upload the file
        blob.upload_from_file(file, content_type=content_type)

        url = blob.generate_signed_url(
            expiration=datetime.timedelta(days=365), method="GET"
        )

        current_datetime = datetime.datetime.utcnow().strftime("%d-%m-%Y")
        data = {
            "download_url": url,
            "upload_datetime": current_datetime,
            "filename": destination_filename,
        }
        cls.cv_collections_ref.add(data)

    # USER MANAGEMENT
    @classmethod
    def user_exists(cls, user_email):
        user = cls.users_ref.where("email", "==", user_email).limit(1).get()
        return len(user) > 0

    @classmethod
    def get_user(cls, user_email):
        user = cls.users_ref.where("email", "==", user_email).limit(1).get()
        return user

    @classmethod
    def update_user(cls, user_email, user_data):
        user = cls.users_ref.where("email", "==", user_email).limit(1).get()
        cls.users_ref.document(user[0].id).update(user_data)
        return cls.get_user(user_email)

    @classmethod
    def delete_user(cls, user_email):
        user = cls.users_ref.where("email", "==", user_email).limit(1).get()
        cls.users_ref.document(user[0].id).delete()

    # CONSULTANCY MANAGEMENT
    @classmethod
    def consultancy_exists(cls, consultancy_email):
        consultancy = (
            cls.consultants_ref.where("email", "==", consultancy_email).limit(1).get()
        )
        return len(consultancy) > 0

    @classmethod
    def get_consultancy(cls, consultancy_email):
        consultancy = (
            cls.consultants_ref.where("email", "==", consultancy_email).limit(1).get()
        )
        return consultancy

    @classmethod
    def update_consultancy(cls, consultancy_email, new_consultancy_account_data):
        consultancy = (
            cls.consultants_ref.where("email", "==", consultancy_email).limit(1).get()
        )
        cls.consultants_ref.document(consultancy[0].id).update(
            new_consultancy_account_data
        )
        return cls.get_consultancy(consultancy_email)

    @classmethod
    def delete_consultancy(cls, consultancy_email):
        consultancy = (
            cls.consultants_ref.where("email", "==", consultancy_email).limit(1).get()
        )
        cls.consultants_ref.document(consultancy[0].id).delete()
