# src/monitor/generate_report.py

import pandas as pd
from evidently.report import Report
from evidently.pipeline.column_mapping import ColumnMapping
from evidently.metric_preset import ClassificationPreset
from google.cloud import storage
import os

def generate_monitoring_report():
    # Cargar los datasets de referencia y actuales
    reference_data = pd.read_csv("data/processed/val_with_preds.csv")
    current_data = pd.read_csv("data/processed/test_with_preds.csv")

    # Definir el mapeo de columnas usando la API moderna
    column_mapping = ColumnMapping(
        target='sentiment',
        prediction='prediction',
        text_features=['review']
    )

    # Inicializar y ejecutar el reporte
    report = Report(metrics=[
        ClassificationPreset(),
    ])

    # El método .run() toma los DataFrames y el column_mapping directamente
    report.run(reference_data=reference_data, 
               current_data=current_data, 
               column_mapping=column_mapping)

    # Guardar el reporte
    os.makedirs("reports", exist_ok=True)
    report.save_html("reports/classification_report.html")
    print("✅ Monitoring report saved at: reports/classification_report.html")

def upload_report_to_gcs(bucket_name: str, destination_blob_name: str, source_file_name: str):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"✅ Report uploaded to gs://{bucket_name}/{destination_blob_name}")

if __name__ == "__main__":
    generate_monitoring_report()