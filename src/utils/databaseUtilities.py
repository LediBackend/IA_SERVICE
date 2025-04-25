from bson import ObjectId
from src.config.database import get_database

# Método para insertar datos en una base de datos específica
def insert_document(db_name, collection_name, data):
    
    db = get_database(db_name)
    
    print(db.list_collection_names()) 
    
    collection = db[collection_name]
    
    result = collection.insert_one(data)
    
    return f"✅ Documento insertado con ID: {result.inserted_id}"

# Método para obtener un documento por filtro
def get_document(db_name, collection_name, query):
    
    db = get_database(db_name)
    collection = db[collection_name]
    result = collection.find_one(query)

    if result:
        return result
    else:
        print("❌ No se encontró ningún documento.")
    return False

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

# Método para actualizar Arrays
def append_to_array(db_name, collection_name, query, field_name, new_value):

    db = get_database(db_name)
    
    collection = db[collection_name]

    result = collection.update_one(query, {"$push": {field_name: new_value}})
    if result.modified_count == 0:
        print('❌ Error al modificar el documento ')
    else:
        print(f"✅ Documentos modificad correctamente")

# Método para eliminar documentos
def delete_document(db_name, collection_name, query):
    db = get_database(db_name)
    collection = db[collection_name]
    result = collection.delete_one(query)
    return f"✅ Documentos eliminados: {result.deleted_count}"

# Método para obtener un documento por su _id
def get_document_by_id(db_name, collection_name, document_id):
    
    db = get_database(db_name)
    
    collection = db[collection_name]
    
    try:
        object_id = ObjectId(document_id)
        result = collection.find_one({"_id": object_id})
        
        if result :
    
            return result
        
        else:
        
            print("❌ No se encontró ningún documento con ese _id.")
        
            return False
    
    except Exception:
    
        return "❌ _id inválido. Asegúrate de que el formato sea correcto."