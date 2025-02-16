# Dockerfile.api
FROM python:3.10-slim

WORKDIR /app

# Instalamos UV globalmente
RUN pip install uv

# Copiamos el archivo de dependencias
COPY requirements.txt .

# Instalamos las dependencias en el sistema usando UV
RUN uv pip install --system -r requirements.txt

# Copiamos el resto de la aplicación (incluyendo main.py, app_streamlit.py, etc.)
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
