# src/monitor/generate_report.py

import pandas as pd
from evidently.report import Report
from evidently.pipeline.column_mapping import ColumnMapping # <-- CAMBIO 1: Importación correcta
from evidently.metric_preset import ClassificationPreset # <-- CAMBIO 2: Importación de Preset actualizada
import os

def generate_monitoring_report():
    # Cargar los datasets de referencia y actuales
    reference_data = pd.read_csv("data/processed/val_with_preds.csv")
    current_data = pd.read_csv("data/processed/test_with_preds.csv")

    # CAMBIO 3: Definir el mapeo de columnas
    # Se reemplaza DataDefinition y Dataset por ColumnMapping
    column_mapping = ColumnMapping(
        target='sentiment',
        prediction='prediction',
        text_features=['review']
    )

    # Inicializar y ejecutar el reporte
    report = Report(metrics=[
        ClassificationPreset(),
    ])

    # CAMBIO 4: El método .run() ahora toma los DataFrames y el column_mapping directamente
    report.run(reference_data=reference_data, 
               current_data=current_data, 
               column_mapping=column_mapping)

    # Guardar el reporte
    os.makedirs("reports", exist_ok=True)
    report.save_html("reports/classification_report.html")
    print("✅ Monitoring report saved at: reports/classification_report.html")

if __name__ == "__main__":
    generate_monitoring_report()