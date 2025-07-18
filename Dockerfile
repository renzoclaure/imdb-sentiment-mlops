# Usa una imagen base ligera con Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el proyecto al contenedor
COPY . .

# Expone el puerto 8080 para Cloud Run
EXPOSE 8080

# Comando de arranque
CMD ["uvicorn", "src.serve.serve_model:app", "--host", "0.0.0.0", "--port", "8080"]
