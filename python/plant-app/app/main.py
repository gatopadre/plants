from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models.plant import Plant
from .services.plant import save, get_all, get_by_id, update, delete

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Esto permite que cualquier origen acceda a la API
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
    allow_headers=["*"],  # Encabezados permitidos
)


# Ruta para la página de inicio
@app.get("/")
async def home():
    return {"message": "Bienvenido a la aplicación de plantas"}


# Ruta para guardar una planta
@app.post("/plant")
async def save_plant(plant: Plant):
    save(plant)
    return {"message": "Planta guardada correctamente"}


# Ruta para obtener el listado de plantas
@app.get('/plant')
async def get_plants():
    return {'message': 'Plantas obtenidas', 'lista_plantas': get_all()}


# Ruta para obtener una planta por su ID
@app.get("/plant/{plant_id}")
async def get_plant_by_id(plant_id: str):
    plant = get_by_id(plant_id)
    if plant:
        return plant
    else:
        raise HTTPException(status_code=404, detail="Planta no encontrada")


# Ruta para actualizar una planta
@app.put("/plant/{plant_id}")
async def update_plant(plant_id: str, plant: Plant):
    plant_id = str(plant_id)
    existing_plant = get_by_id(plant_id)
    if existing_plant:
        update(plant)
        return {"message": "Planta actualizada correctamente"}
    else:
        raise HTTPException(status_code=404, detail="Planta no encontrada")


# Ruta para eliminar una planta por su ID
@app.delete("/plant/{plant_id}")
async def delete_plant(plant_id: str):
    plant_id = str(plant_id)
    existing_plant = get_by_id(plant_id)
    if existing_plant:
        delete(plant_id)
        return {"message": "Planta eliminada correctamente"}
    else:
        raise HTTPException(status_code=404, detail="Planta no encontrada")


# Manejo de errores 404
@app.exception_handler(HTTPException)
async def not_found(request, exc):
    return {"error": "No encontrado"}


# Manejo de errores 500
@app.exception_handler(Exception)
async def server_error(request, exc):
    return {"error": "Error interno del servidor"}

# Si deseas, puedes agregar más rutas y lógica de aplicación aquí

# Si deseas ejecutar la aplicación desde este archivo directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
