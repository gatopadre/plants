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
