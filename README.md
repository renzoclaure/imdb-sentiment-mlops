# IMDb Sentiment Analysis - MLOps Project

## 📌 Project Description

This project presents an end-to-end Machine Learning pipeline for classifying IMDb TV show reviews by sentiment (positive or negative). It integrates core MLOps components, such as experiment tracking, deployment, orchestration, and monitoring.

## 💡 Problem Description

Users often rely on reviews to decide whether to watch a show. Automatically classifying sentiment in IMDb reviews can help platforms recommend content and better understand user feedback. This project solves the problem of automating sentiment classification using an ML model deployed and monitored in production.

## 🚀 Features

- Model Training with `LogisticRegression` and `TfidfVectorizer`
- Experiment tracking and model registry with MLflow
- Model deployment using FastAPI, Docker and Cloud Run (GCP)
- Monitoring with Evidently + Airflow + GCS
- Workflow orchestration with Apache Airflow
- Cloud-based artifacts and bucket integration (GCS)
- Testing and reproducibility best practices

## ☁️ Cloud Components

- Google Cloud Storage (GCS)
- Google Cloud Run
- Artifact Registry

## 🧪 Experiment Tracking

- MLflow tracks experiments, parameters, and metrics
- Model artifacts saved and logged in MLflow

## 🔁 Workflow Orchestration

- DAG defined in Airflow for generating monitoring report and uploading it to GCS

## 🧼 Monitoring

- Evidently used for generating a classification metrics report
- HTML report saved and uploaded to a public GCS bucket

## 🧪 Tests

Basic test for model training logic using Pytest included in `tests/test_train.py`.

## ⚙️ How to Run

1. Clone the repo and create the environment:
    ```bash
    conda env create -f environment.yml
    conda activate imdb_sentiment_env
    ```

2. Train and log the model:
    ```bash
    python src/train/train.py
    ```

3. Serve the model with FastAPI locally:
    ```bash
    python src/serve/serve_model.py
    ```

4. Generate monitoring report:
    ```bash
    python src/monitor/generate_report.py
    ```

5. Run tests:
    ```bash
    pytest tests/
    ```

## 🐳 Docker & Cloud Deployment

- Build and push Docker image to Artifact Registry
- Deploy with:
    ```bash
    gcloud run deploy sentiment-api --image <your_image_path> --region us-central1 --allow-unauthenticated
    ```

## 📊 Monitoring Report

You can access the latest monitoring report at:  
👉 https://storage.googleapis.com/imdb-monitoring-renzo/reports/classification_report.html

## ✅ Evaluation Criteria Covered

- [x] Problem clearly described
- [x] Uses cloud for deployment and monitoring (GCP)
- [x] MLflow used for tracking and registry
- [x] Airflow used for workflow orchestration
- [x] Model deployed on Cloud Run with Docker
- [x] Model monitoring with Evidently
- [x] Reproducible environment (`environment.yml`, `Makefile`)
- [x] Basic test + Makefile + CI-ready structure

---

Created by Renzo for the MLOps Zoomcamp Final Project.