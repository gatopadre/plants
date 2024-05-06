from pydantic import BaseModel
from ..db.mongoDB.mongo_conection import MongoDB


# Definición del modelo de datos para la planta
class Plant(BaseModel):
    name: str

    class Config:
        # Nombre de la colección en MongoDB
        __collection__ = "Plants"

    def save(self):
        # Convertir el modelo Plant a un diccionario
        plant_data = self.dict()
        # Guardar los datos de la planta en la base de datos MongoDB
        database = MongoDB()
        database.save_to_bd(plant_data, self.Config.__collection__)  # Pasar los datos y el nombre de la colección

    @staticmethod
    def get_all():
        mongo = MongoDB()
        plants = mongo.get_all_from_bd(Plant.Config.__collection__)  # Obtener todas las plantas de la colección
        return plants
