# src/train/train.py

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://localhost:5000")

def load_data():
    train = pd.read_csv("data/processed/train.csv")
    val = pd.read_csv("data/processed/val.csv")
    return train, val


def train_model(train_df, val_df):
    X_train = train_df["review"]
    y_train = train_df["sentiment"]

    X_val = val_df["review"]
    y_val = val_df["sentiment"]

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    # Grid search (opcional)
    param_grid = {
        "tfidf__min_df": [5],
        "tfidf__ngram_range": [(1, 2)],
        "clf__C": [1.0],
    }

    grid = GridSearchCV(pipeline, param_grid, cv=3, verbose=1, n_jobs=-1)

    with mlflow.start_run():
        grid.fit(X_train, y_train)
        preds = grid.predict(X_val)
        report = classification_report(y_val, preds, output_dict=True)

        mlflow.log_params(grid.best_params_)
        mlflow.log_metrics({
            "f1_macro": report["macro avg"]["f1-score"],
            "accuracy": report["accuracy"],
        })

        mlflow.sklearn.log_model(grid.best_estimator_, artifact_path="model", registered_model_name="imdb_sentiment_model")

        print("Training complete. Model logged and registered.")


def main():
    train_df, val_df = load_data()
    train_model(train_df, val_df)


if __name__ == "__main__":
    main()
