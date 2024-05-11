from pymongo import MongoClient, ReturnDocument
from dotenv import load_dotenv
import os
from pathlib import Path


class MongoDB:
    def __init__(self):
        self._connect_to_database()

    def _connect_to_database(self):
        # Ruta del directorio actual
        current_dir = Path(__file__).resolve().parent

        # Ruta del archivo .env
        env_path = current_dir.parent.parent.parent / ".env"

        # Cargar las variables de entorno desde el archivo .env
        load_dotenv(env_path)

        # Obtener la URL de MongoDB desde las variables de entorno
        uri = os.getenv("MONGODB_URI")
        db_name = os.getenv("MONGODB_DB_NAME")

        # Conexión a MongoDB
        self.client = MongoClient(uri)
        self.db = self.client[db_name]  # Nombre de tu base de datos

    @staticmethod
    def save_to_db(data, collection_name):
        mongo = MongoDB()
        collection = mongo.db[collection_name]
        collection.insert_one(data)

    @staticmethod
    def get_all_from_db(collection_name):
        mongo = MongoDB()
        collection = mongo.db[collection_name]
        # Obtener todos los documentos de la colección
        data = list(collection.find())
        # Convertir los ObjectId a cadenas utilizando map
        data = list(map(lambda data: {**data, "_id": str(data["_id"])}, data))
        return data

    @staticmethod
    def get_by_id_from_db(collection_name, id_data):
        mongo = MongoDB()
        collection = mongo.db[collection_name]
        return collection.find_one({"_id": id_data})

    @staticmethod
    def update_in_db(data, collection_name):
        mongo = MongoDB()
        collection = mongo.db[collection_name]
        id_data = data["_id"]
        del data["_id"]
        collection.find_one_and_update({"_id": id_data}, {"$set": data}, return_document=ReturnDocument.AFTER)

    @staticmethod
    def delete_from_db(collection_name, id_data):
        mongo = MongoDB()
        collection = mongo.db[collection_name]
        collection.delete_one({"_id": id_data})
