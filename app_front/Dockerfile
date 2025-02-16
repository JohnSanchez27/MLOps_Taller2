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

EXPOSE 8501

CMD ["streamlit", "run app_streamlit.py", "--host", "0.0.0.0", "--port", "8501"]
