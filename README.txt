# IMDb Sentiment Analysis - MLOps Zoomcamp Final Project

This project demonstrates a complete MLOps pipeline applied to a sentiment analysis model on TV show reviews using the `imdb_tvshows.csv` dataset.

---

## 🔧 Technologies Used

- Python
- Scikit-learn
- MLflow
- Evidently
- Docker
- Airflow
- Google Cloud Platform (GCP): Storage + Cloud Run

---

## 📁 Project Structure

```
imdb_sentiment_project/
├── data/
│   └── raw/                  <- Original file `imdb_tvshows.csv`
├── src/
│   ├── data/                 <- Cleaning, splitting, preprocessing
│   ├── train/                <- Training with MLflow and GridSearchCV
│   ├── serve/                <- FastAPI + MLflow API
│   └── monitor/              <- Evidently report and GCS upload
├── dags/                     <- Airflow DAG for monitoring
├── models/                   <- Exported model
├── reports/                  <- Generated HTML report
├── requirements.txt
└── docker-compose.yaml
```

---

## ⚙️ Project Flow

1. **Ingestion and preprocessing**
   - Clean and split the dataset into train, val, test.

2. **Training**
   - Train a model using `TfidfVectorizer` + `LogisticRegression`.
   - Model is registered with MLflow.

3. **Deployment**
   - Model is packaged in Docker and pushed to GCP.
   - API exposed via Cloud Run with `/predict` endpoint.

4. **Monitoring**
   - Evidently report compares validation vs test set.
   - Report is uploaded to GCS automatically.

---

## 🔍 Final Results

- Prediction API endpoint (FastAPI):
  ```
  https://sentiment-api-417391075761.us-central1.run.app/predict
  ```

- Monitoring report:
  ```
  https://storage.googleapis.com/imdb-monitoring-renzo/reports/classification_report.html
  ```

---

## ✅ How to Run

1. Create environment:
   ```
   pip install -r requirements.txt
   ```

2. Start Airflow:
   ```
   docker-compose up airflow-init
   docker-compose up
   ```

3. Train model:
   ```
   python src/train/train.py
   ```

4. Test API:
   ```
   curl -X POST -H "Content-Type: application/json" \
     -d '{"text": "This show was amazing!"}' \
     https://sentiment-api-417391075761.us-central1.run.app/predict
   ```

5. Trigger DAG manually from Airflow UI.

---

## 🧹 Optional Production Improvements

- Use `KubernetesExecutor` or `CeleryExecutor`.
- Automate ingestion and retraining.
- Add alerting if model performance degrades (Evidently).

---

## 👨‍💻 Author

Renzo Claure  
Final Project - MLOps Zoomcamp 2025
