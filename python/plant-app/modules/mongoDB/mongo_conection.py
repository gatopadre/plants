from pymongo import MongoClient

class MongoDB:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client['PlantApp']  # Nombre de tu base de datos
        self.plants_collection = self.db['Plants']  # Nombre de tu colección de plantas

    def save_plant(self, plant_data):
        self.plants_collection.insert_one(plant_data)

    # Puedes agregar más métodos según sea necesario, como recuperar plantas, actualizar, eliminar, etc.
