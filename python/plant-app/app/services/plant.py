from ..models.plant import Plant

# Servicio para guardar una planta


def save(plant: Plant):
    # Crear una instancia de la planta y luego guardarla
    new_plant = Plant(**plant.dict())
    new_plant.save()

# Servicio para obtener todas las plantas


def get_all():
    # Obtener todas las instancias de plantas y devolverlas como una lista
    return Plant.get_all()

# Servicio para obtener una planta por su ID


def get_by_id(plant_id: str):
    # Obtener la planta por su ID y devolverla
    return Plant.get_by_id(plant_id)

# Servicio para actualizar una planta


def update(plant: Plant):
    # Actualizar los datos de la planta
    plant.update()

# Servicio para eliminar una planta por su ID


def delete(plant_id: str):
    # Eliminar la planta por su ID
    Plant.delete(plant_id)
