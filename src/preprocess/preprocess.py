# src/preprocess/preprocess.py

import os
import pandas as pd
from sklearn.model_selection import train_test_split


def label_sentiment(rating):
    """Convierte rating numérico en sentimiento categórico"""
    if rating >= 8:
        return "positive"
    elif rating <= 4:
        return "negative"
    else:
        return "neutral"


def preprocess(df):
    # Drop columnas innecesarias o nulas
    df = df.dropna(subset=["Rating (out of 10)", "Review"])
    df = df[["Review", "Rating (out of 10)"]].copy()
    df.rename(columns={"Rating (out of 10)": "rating", "Review": "review"}, inplace=True)

    # Crear la etiqueta de sentimiento
    df["sentiment"] = df["rating"].apply(label_sentiment)

    return df


def split_and_save(df, output_dir="data/processed", test_size=0.2, val_size=0.1, random_state=42):
    train_val, test = train_test_split(df, test_size=test_size, stratify=df["sentiment"], random_state=random_state)
    train, val = train_test_split(train_val, test_size=val_size, stratify=train_val["sentiment"], random_state=random_state)

    os.makedirs(output_dir, exist_ok=True)

    train.to_csv(os.path.join(output_dir, "train.csv"), index=False)
    val.to_csv(os.path.join(output_dir, "val.csv"), index=False)
    test.to_csv(os.path.join(output_dir, "test.csv"), index=False)

    print(f"Train: {len(train)} rows")
    print(f"Val:   {len(val)} rows")
    print(f"Test:  {len(test)} rows")


def main():
    input_path = os.path.join("data", "raw", "imdb_tvshows.csv")
    df = pd.read_csv(input_path)
    df_clean = preprocess(df)
    split_and_save(df_clean)


if __name__ == "__main__":
    main()
