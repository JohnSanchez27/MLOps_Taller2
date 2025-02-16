from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from domain.to_dataframe import to_dataframe
from cargar_modelos import cargar_modelos
from collections import Counter
import re
import time
import threading  

app = FastAPI()

class Pinguino(BaseModel):
    culmen_length_mm: float
    culmen_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    island: str
    sex: str
    
modelos_name = {}
for clave, valor in cargar_modelos().items():
    if clave != "column_order":
        valor_limpio = re.sub(r'\(.*?\)', '', str(valor))
        modelos_name [clave] = valor_limpio
        
modelos_name_lock = threading.Lock()  # Crea un bloqueo para proteger modelos_name
def actualizar_modelos():
    global modelos_name
    while True:
        nuevos_modelos = {}
        for clave, valor in cargar_modelos().items():
            if clave != "column_order":
                valor_limpio = re.sub(r'\(.*?\)', '', str(valor))
                nuevos_modelos[clave] = valor_limpio
        with modelos_name_lock:  # Adquiere el bloqueo antes de modificar modelos_name
            modelos_name = nuevos_modelos  # Actualiza la variable global
            
        print("Modelos actualizados:", modelos_name)
        time.sleep(3600)

# Inicia el hilo en segundo plano para actualizar modelos
thread = threading.Thread(target=actualizar_modelos, daemon=True)
thread.start()

@app.post("/pinguino")
def postPinguino(pinguino: Pinguino):
    print("iciaa")
    df = to_dataframe(pinguino)# tranforma mi calse pinguino en un dataframe como el que se uso para entenerar los modelos
    modelos= cargar_modelos()# carga los modelos entreandos
    print(modelos)
    df = df[ modelos['column_order']]# define el orden de las columnas igual a las del modelo entrenado
    listaInferencia = [modelos[f'modelo{i}'].predict(df).tolist()[0] for i in range(1, 5)]#crea una lista de los modelos 
    # Función lambda para encontrar el elemento más frecuente (directamente en la línea)
    elemento_mas_frecuente = lambda lista: (lambda c: (lambda: c.most_common(1)[0][0])() if c else None)(Counter(lista))
    elemento_mas_comun = elemento_mas_frecuente(listaInferencia)
    print(elemento_mas_comun)
    return {"message": "Pinguino recibido", "data": elemento_mas_comun}

@app.post("/pinguino/{modelo}")
def postPinguino(pinguino: Pinguino, modelo:str):

    df = to_dataframe(pinguino)# tranforma mi calse pinguino en un dataframe como el que se uso para entenerar los modelos
    modelos= cargar_modelos()# carga los modelos entreandos
    df = df[ modelos['column_order']]# define el orden de las columnas igual a las del modelo entrenado
    inferencia = modelos[modelo].predict(df)    
    print("data :", inferencia)
    return {"Modelo Usado ": modelos_name[modelo], "Inferencia":   inferencia[0]}

@app.get("/pinguino/model")
def obtener_modelos():
    
    modelos_name = {}
    for clave, valor in cargar_modelos().items():
        if clave != "column_order":
            valor_limpio = re.sub(r'\(.*?\)', '', str(valor))  # Elimina paréntesis y contenido            
            modelos_name[valor_limpio] = clave
    if  modelos_name is None:
        return {"error": "No se pudieron cargar los modelos"}
    return modelos_name