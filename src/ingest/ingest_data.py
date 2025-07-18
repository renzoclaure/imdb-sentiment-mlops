# src/ingest/ingest_data.py

import os
from google.cloud import storage
import pandas as pd
from datetime import datetime

def upload_to_gcs(bucket_name, source_file_path, destination_blob_name):
    client = storage.Client(project="dtc-de-course-456314")

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_path)
    print(f"File {source_file_path} uploaded to {destination_blob_name} in bucket {bucket_name}.")


def main():
    local_path = os.path.join("data", "raw", "imdb_tvshows.csv")
    bucket_name = "imdb-sentiment-bucket-renzo"
    
    # Nombre remoto incluye fecha para versionar
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    remote_path = f"raw/imdb_tvshows_{timestamp}.csv"
    
    df = pd.read_csv(local_path)
    print(f"Loaded {len(df)} records from {local_path}")
    
    upload_to_gcs(bucket_name, local_path, remote_path)


if __name__ == "__main__":
    main()
