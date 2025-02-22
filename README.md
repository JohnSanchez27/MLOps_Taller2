# Predicción de Especies de Pingüinos con Jupyter, FastAPI y Streamlit

## 📌 Descripción del Proyecto

Este proyecto utiliza **Docker Compose** para orquestar múltiples servicios, incluyendo una API backend, una aplicación frontend y un entorno de desarrollo con JupyterLab. Se emplea un volumen compartido para almacenar modelos.

Adicionalmente, Este proyecto cuenta con tres servicios principales: un backend basado en FastAPI (api_back) que expone el **puerto 8000**, un frontend con Streamlit (api_front) en el **puerto 8501**, y un entorno de desarrollo interactivo con JupyterLab (jupyter) en el **puerto 8888**. Todos los servicios comparten el volumen models_volume para el almacenamiento de modelos.

---

## 🛠 Tecnologías Utilizadas

- **🐍 Python 3.10-slim**
- **🚀 FastAPI** (Para la creación del API REST)
- **🎨 Streamlit** (Para la interfaz gráfica del usuario)
- **📊 Scikit-learn** (Para entrenamiento de modelos de Machine Learning)
- **🐳 Docker** (Para la contenedorización y despliegue)
- **![image](https://github.com/user-attachments/assets/00de2200-517d-4029-b770-c5b29ffb6ab6) Docker Compose** (Para orquestar contenedores)
- **⚡ Uvicorn** (Para ejecutar FastAPI)
- **💾 Joblib & Pickle** (Para serialización de modelos)

---

## 🚀 Instrucciones de Instalación y Ejecución

### 1️⃣ Clonar el Repositorio
```bash
 git clone git@github.com:JohnSanchez27/MLOps_Taller2.git
 cd MLOps_Taller2
```

### 2️⃣ Construir y Ejecutar el Contenedor Docker

Para construir y ejecutar los contenedores:
```bash
docker-compose up --build
```

Para detener los contenedores sin eliminarlos::
```bash
docker-compose stop
```
**Nota: Volúmenes Compartidos**: Este proyecto utiliza un volumen persistente models_volume para compartir modelos entre los diferentes servicios.

Esto iniciará la API en el puerto **8989** y la interfaz de Streamlit en el puerto **8501**.

### 3️⃣ Acceder a la API, la Interfaz Gráfica y Jupyter

- 📌 **API Docs**: Para acceder a la API Backend, visita: [http://localhost:8000]
- 🖥 **Interfaz Streamlit**: ara acceder a la interfaz en Streamlit, visita: [http://localhost:8501]
- 🎖 **Jupyter** :Para acceder a JupyterLab, visita: [http://localhost:8888]

---

### 4️⃣ Uso de JupyterLab

JupyterLab proporciona un entorno interactivo donde puedes analizar datos, entrenar modelos y guardarlos en la carpeta models. Para trabajar con JupyterLab:

➕ Crear un Nuevo Notebook

Accede a http://localhost:8888

En el panel lateral izquierdo, selecciona la carpeta notebooks.

Haz clic en New y selecciona Python 3 Notebook.

📂 Guardar Modelos en la Carpeta models

Si entrenas un modelo en Jupyter y deseas que FastAPI lo cargue automáticamente, sigue estos pasos:

```python
import joblib

# Entrenar y guardar el modelo
modelo = ... # Define tu modelo aquí
joblib.dump(modelo, "/models/nuevo_modelo.pkl")

```

FastAPI reconocerá automáticamente el nuevo modelo y podrá usarlo para predicciones.

## 📂 Estructura del Proyecto

La estructura del proyecto está organizada en diferentes directorios para separar los servicios y recursos. app_back contiene el código de la API backend con FastAPI, 
app_front alberga la interfaz de usuario construida con Streamlit, y jupyter proporciona un entorno interactivo con JupyterLab. Además, models_volume actúa como almacenamiento 
compartido para modelos de machine learning en formato **.pkl.** El archivo **docker-compose.yml** define y configura la ejecución de todos los servicios en contenedores Docker.

```bash
Taller_2/
│── app_back/
│   │── domain/
│   │── cargar_modelos.py
│   │── Dockerfile
│   │── main.py
│   │── requirements.txt
│
│── app_front/
│   │── app_streamlit.py
│   │── Dockerfile
│   │── requirements.txt
│
│── jupyter/
│   │── data/
│   │── Dockerfile
│   │── requirements.txt
│
│── models_volume/
│   │── notebook/
│   │── column_order.pkl
│   │── modelo1.pkl
│   │── modelo2.pkl
│   │── modelo3.pkl
│   │── modelo4.pkl
│   │── modelo22.pkl
│   │── modelo23.pkl
│   │── modelo24.pkl
│   │── nuevo_modelo.pkl  # Modelos nuevos creados en Jupyter
│
│── docker-compose.yml
```

---

## 🔗 Funcionamiento del API

La API permite realizar inferencias sobre la especie de un pingüino basándose en distintas características. 

### **1️⃣ Inferencia con todos los modelos**
🔹 Devuelve la predicción basada en el modelo con mayor consenso.
   - **📌 Endpoint:** `POST /pinguino`
   - **📩 Entrada:** Datos del pingüino en formato JSON.
   - **📤 Salida:** Predicción de la especie del pingüino.

### **2️⃣ Inferencia con un modelo específico**
🔹 El usuario puede seleccionar el modelo de Machine Learning a utilizar.
   - **📌 Endpoint:** `POST /pinguino/{modelo}`
   - **📩 Entrada:** Datos del pingüino y el nombre del modelo a utilizar.
   - **📤 Salida:** Predicción basada en el modelo seleccionado.

#### **Ejemplo de solicitud JSON:**
```json
{
  "culmen_length_mm": 50.0,
  "culmen_depth_mm": 18.0,
  "flipper_length_mm": 200.0,
  "body_mass_g": 5000,
  "island": "Torgersen",
  "sex": "MALE"
}
```

---

## 🤖 Modelos Implementados

Se han entrenado cuatro modelos de Machine Learning:

- ✅ **K-Nearest Neighbors (modelo1)**
- ✅ **Support Vector Machine (modelo2)**
- ✅ **Naive Bayes (modelo3)**
- ✅ **Perceptrón Multicapa (modelo4)**

Estos modelos han sido entrenados utilizando el dataset de pingüinos y evaluados con una partición de datos de entrenamiento y prueba; Sin embargo, como se estan utilizando volumenes compartidos, se entrenaron 3 modelos adicionales con el fin de garantizar que se puedan agregar mas modelos y que la APP los pueda consumir sin ningun problema. 

- ✅ **Árbol de Decisión (modelo22)**
- ✅ **Random Forest o Bosque Aleatorio (modelo23)**
- ✅ **Gradient Boosting (modelo24)**

Cómo se explicó en la sección anterior, usted también puede crear nuevos modelos o eliminar existentes.
  
---

## 🎨 Implementación de Streamlit

La aplicación de **Streamlit** permite a los usuarios interactuar con la API de manera visual. Desde la interfaz, el usuario puede:

1️⃣ Ingresar las características de un pingüino.  
2️⃣ Seleccionar el modelo de Machine Learning.  
3️⃣ Obtener la predicción en tiempo real.  

Así deberás ver la interfaz:

![image](https://github.com/user-attachments/assets/eb791f28-e0fa-4ad7-ba9f-ca0816f66daf)


---
