from pydantic import BaseModel
from pymongo.errors import PyMongoError
from ..db.mongoDB.mongo_conection import MongoDB as database


# Definición del modelo de datos para la planta
class Plant(BaseModel):
    name: str

    class Config:
        # Nombre de la colección en MongoDB
        __collection__ = "Plants"

    def save(self):
        # Convertir el modelo Plant a un diccionario
        plant_data = self.dict()
        try:
            # Guardar los datos de la planta en la base de datos MongoDB
            database.save_to_db(plant_data, self.Config.__collection__)
        except PyMongoError as e:
            # Manejar el error de MongoDB de alguna manera (registro, notificación, etc.)
            print(f"Error al guardar la planta en la base de datos: {e}")

    @staticmethod
    def get_all():
        plants = database.get_all_from_db(Plant.Config.__collection__)
        return plants

    @staticmethod
    def get_by_id(plant_id):
        plant = database.get_by_id_from_db(Plant.Config.__collection__, plant_id)
        return plant

    def update(self):
        # Convertir el modelo Plant a un diccionario
        plant_data = self.dict()
        try:
            # Actualizar los datos de la planta en la base de datos MongoDB
            database.update_in_db(plant_data, self.Config.__collection__)
        except PyMongoError as e:
            # Manejar el error de MongoDB de alguna manera (registro, notificación, etc.)
            print(f"Error al actualizar la planta en la base de datos: {e}")

    @staticmethod
    def delete(plant_id):
        try:
            # Eliminar la planta de la base de datos MongoDB
            database.delete_from_db(Plant.Config.__collection__, plant_id)
        except PyMongoError as e:
            # Manejar el error de MongoDB de alguna manera (registro, notificación, etc.)
            print(f"Error al eliminar la planta de la base de datos: {e}")
