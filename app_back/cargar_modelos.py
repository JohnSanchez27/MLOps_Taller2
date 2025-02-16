import joblib
import os

def cargar_modelos():
 
    try:

        # Definir el directorio de modelos
        models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")

        # Obtener todos los archivos en el directorio que sigan el patrón "modeloX.pkl"
        modelos = {}
        for filename in os.listdir(models_dir):
            if filename.startswith("modelo") and filename.endswith(".pkl"):
                key = filename.replace(".pkl", "")  # Eliminar la extensión para usarla como clave
                modelos[key] = joblib.load(os.path.join(models_dir, filename))

        # Cargar el archivo "column_order.pkl" si existe
        column_order_path = os.path.join(models_dir, "column_order.pkl")
        if os.path.exists(column_order_path):
            modelos["column_order"] = joblib.load(column_order_path)



        return modelos
    

    
    except FileNotFoundError:
        print(f"Error: No se encontraron los archivos .pkl en la carpeta models: {os.path.join(models_dir, 'modelo1.pkl')}")
        return None
    except Exception as e:
        print(f"Error al cargar los modelos: {e}")
        return None