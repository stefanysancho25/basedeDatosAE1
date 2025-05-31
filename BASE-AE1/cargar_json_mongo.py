import json
from pymongo import MongoClient

#    Conexión a MongoDB
cliente = MongoClient('mongodb://localhost:27017/')
db = cliente.db_no_relacional
coleccion = db.empleados  # Puedes cambiar el nombre de la colección si lo deseas

# Leer el archivo JSON
with open('data.json', encoding='utf-8') as f:
    datos = json.load(f)

# Insertar los datos en la colección
if isinstance(datos, list):
    coleccion.insert_many(datos)
    print(f"Se insertaron {len(datos)} documentos en la colección 'empleados'.")
else:
    coleccion.insert_one(datos)
    print("Se insertó 1 documento en la colección 'empleados'.")

