import pymongo
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("❌ No se encontró la variable MONGO_URI en el entorno.")

# Conectar con MongoDB Atlas
client = pymongo.MongoClient(MONGO_URI)

def get_database(db_name):
    """Devuelve una base de datos específica del cluster."""
    return client[db_name]

print("✅ Conexión exitosa con MongoDB Atlas")
