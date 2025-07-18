from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Add project root to PYTHONPATH so Airflow can find src/
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from src.train.train import main as train_main  # ← importamos la función principal

default_args = {
    "owner": "renzo",
    "start_date": datetime(2025, 7, 17),
    "retries": 1,
}

with DAG(
    dag_id="train_model_pipeline",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description="Train sentiment classifier and log to MLflow",
) as dag:

    train_model_task = PythonOperator(
        task_id="train_model",
        python_callable=train_main,
    )

    train_model_task
