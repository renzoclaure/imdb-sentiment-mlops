import sys
import os
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Asegurar ruta a src
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

# Importar funciones después de modificar sys.path
from monitor.generate_report import generate_monitoring_report, upload_report_to_gcs

default_args = {
    "owner": "renzo",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

# Función 100% serializable para subir el reporte
def upload_report():
    upload_report_to_gcs(
        bucket_name="imdb-monitoring-renzo",
        destination_blob_name="reports/classification_report.html",
        source_file_name="reports/classification_report.html"
    )

with DAG(
    dag_id="monitor_metrics_dag",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description="Genera el reporte de monitoreo con Evidently y lo sube a GCS",
) as dag:

    task_generate_report = PythonOperator(
        task_id="generate_monitoring_report",
        python_callable=generate_monitoring_report,
    )

    task_upload_report = PythonOperator(
        task_id="upload_report_to_gcs",
        python_callable=upload_report,
    )

    task_generate_report >> task_upload_report
