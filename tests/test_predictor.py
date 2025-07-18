# tests/test_predictor.py

import pytest
import mlflow.sklearn
import os

def test_model_prediction():
    model_path = "sentiment_model"
    
    # Verifica que el modelo existe
    assert os.path.exists(model_path), f"Model path '{model_path}' does not exist"
    
    # Carga el modelo registrado con MLflow
    model = mlflow.sklearn.load_model(model_path)

    # Prueba con una reseña de ejemplo
    sample_input = ["This was a very disappointing movie."]
    prediction = model.predict(sample_input)

    # Verifica que el resultado sea una lista con una predicción válida (0 o 1)
    assert prediction.shape[0] == 1
    assert prediction[0] in [0, 1]
