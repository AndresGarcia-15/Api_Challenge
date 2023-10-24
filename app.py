from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import uvicorn

# Initializing the FastAPI app
app = FastAPI()
app.title = "DATOS CHALLENGE"

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carga el contenido del archivo JSON al iniciar la aplicación
with open("datos_filtrados_con_Rm_ind1.11.json", "r") as json_file:
    data_storage = json.load(json_file)

# Ruta para obtener todos los datos entre dos fechas
@app.get("/data/")
async def get_data(fecha_inicio: str, fecha_fin: str):
    # Filtrar los datos que estén dentro del rango de fechas dado
    filtered_data = [item for item in data_storage if fecha_inicio <= item.get("datetime") <= fecha_fin]
    return filtered_data

if __name__ == "__main":
    uvicorn.run(app, host="localhost", port=8000)