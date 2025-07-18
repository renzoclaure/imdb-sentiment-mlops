import pandas as pd
import mlflow.pyfunc
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")  # 👈 Agregá esta línea antes de cargar el modelo

# Cargar modelo desde MLflow
model_uri = "models:/imdb_sentiment_model/Production"
model = mlflow.pyfunc.load_model(model_uri)

def add_predictions(input_path: str, output_path: str):
    df = pd.read_csv(input_path)

    # Predecir usando solo la columna 'review'
    df["prediction"] = model.predict(df["review"])

    # Guardar nuevo archivo con predicciones
    df.to_csv(output_path, index=False)
    print(f"✅ Predicciones guardadas en {output_path}")

if __name__ == "__main__":
    add_predictions("data/processed/val.csv", "data/processed/val_with_preds.csv")
    add_predictions("data/processed/test.csv", "data/processed/test_with_preds.csv")
