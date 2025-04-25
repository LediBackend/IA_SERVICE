from src.config.database import get_database

# Método para insertar datos en una base de datos específica
def insert_document(db_name, collection_name, data):
    db = get_database(db_name)
    collection = db[collection_name]
    result = collection.insert_one(data)
    return f"✅ Documento insertado con ID: {result.inserted_id}"

# Método para obtener un documento por filtro
def get_document(db_name, collection_name, query):
    db = get_database(db_name)
    collection = db[collection_name]
    result = collection.find_one(query)
    return result if result else "❌ No se encontró ningún documento."

# Método para obtener todos los documentos en una colección
def get_all_documents(db_name, collection_name):
    db = get_database(db_name)
    collection = db[collection_name]
    return list(collection.find())

# Método para actualizar documentos
def update_document(db_name, collection_name, query, new_values):
    db = get_database(db_name)
    collection = db[collection_name]
    result = collection.update_one(query, {"$set": new_values})
    return f"✅ Documentos modificados: {result.modified_count}"

# Método para eliminar documentos
def delete_document(db_name, collection_name, query):
    db = get_database(db_name)
    collection = db[collection_name]
    result = collection.delete_one(query)
    return f"✅ Documentos eliminados: {result.deleted_count}"
