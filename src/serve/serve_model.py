# src/serve/serve_model.py

from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import uvicorn
import os

app = FastAPI()

# Load the model from a local path inside the container
model = mlflow.sklearn.load_model("sentiment_model")

class ReviewInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Sentiment model is ready"}

@app.post("/predict")
def predict_sentiment(review: ReviewInput):
    prediction = model.predict([review.text])
    return {"text": review.text, "predicted_sentiment": prediction[0]}

if __name__ == "__main__":
    uvicorn.run("src.serve.serve_model:app", host="0.0.0.0", port=8080)
