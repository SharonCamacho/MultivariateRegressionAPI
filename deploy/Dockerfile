# Imagen base con Python y dependencias esenciales
FROM python:3.13-slim

WORKDIR /app

# Actualizar pip e instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Establecer PYTHONPATH
ENV PYTHONPATH=/app

# Exponer el puerto de FastAPI
EXPOSE 8080

# Definir variables de entorno
ENV ENVIRONMENT=production
ENV PORT=8080

# Comando de inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]