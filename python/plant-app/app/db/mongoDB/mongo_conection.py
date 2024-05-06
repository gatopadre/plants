from pymongo import MongoClient


class MongoDB:
    def __init__(self):
        # Conexión a MongoDB
        uri = 'mongodb+srv://sebastianzunigasaavedra:Sebastian@plantapp.03vptpo.mongodb.net/?retryWrites=true&w=majority&appName=PlantAPP'
        self.client = MongoClient(uri)
        self.db = self.client['PlantApp']  # Nombre de tu base de datos

    def save_to_bd(self, data, collection_name):
        collection = self.db[collection_name]
        collection.insert_one(data)

    def get_all_from_bd(self, collection_name):
        collection = self.db[collection_name]
        # Obtén todos los documentos de la colección
        documents = list(collection.find({}))
        # Convierte manualmente los ObjectId a strings
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        return documents
    # Puedes agregar más métodos según sea necesario, como recuperar plantas, actualizar, eliminar, etc.
