FROM python:3.10-slim

WORKDIR /app

# Instalamos UV globalmente
RUN pip install uv

# Copiamos el archivo de dependencias
COPY . .

# Instalamos las dependencias en el sistema
RUN uv pip install --system -r requirements.txt

# Instalamos JupyterLab en el sistema
RUN uv pip install --system jupyterlab

# Copiamos el resto del código
COPY . .

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
