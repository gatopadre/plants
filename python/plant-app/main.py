from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from modules.mongoDB.mongo_conection import MongoDB
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Esto permite que cualquier origen acceda a la API
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
    allow_headers=["*"],  # Encabezados permitidos
)

# Conexión a MongoDB
mongo = MongoDB("mongodb+srv://sebastianzunigasaavedra:Sebastian@plantapp.03vptpo.mongodb.net/?retryWrites=true&w=majority&appName=PlantAPP")

# Definición del modelo de datos para la planta
class Plant(BaseModel):
    name: str

# Ruta para la página de inicio
@app.get("/")
async def home():
    return {"message": "Bienvenido a la aplicación de plantas"}

# Ruta para guardar una planta
@app.post("/plant")
async def save_plant(plant: Plant):
    plant_data = {"name": plant.name}
    mongo.save_plant(plant_data)
    return {"message": "Planta guardada correctamente"}

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
