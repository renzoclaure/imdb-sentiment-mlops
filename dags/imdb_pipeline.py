# dags/imdb_pipeline.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Add project root to PYTHONPATH
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from src.ingest.ingest_data import main as ingest_main
from src.preprocess.preprocess import main as preprocess_main

default_args = {
    "owner": "renzo",
    "start_date": datetime(2025, 7, 17),
    "retries": 1,
}

with DAG(
    dag_id="imdb_ingest_preprocess",
    default_args=default_args,
    schedule_interval=None,  # Solo se ejecuta manualmente por ahora
    catchup=False,
    description="Ingest and preprocess IMDb TV reviews",
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_data",
        python_callable=ingest_main,
    )

    preprocess_task = PythonOperator(
        task_id="preprocess_data",
        python_callable=preprocess_main,
    )

    ingest_task >> preprocess_task
