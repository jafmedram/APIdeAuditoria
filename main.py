from fastapi import FastAPI
from src.index import index
from src.equipos import obtener_equipos, obtener_equipo, agregar_equipo

app = FastAPI()

# Registrar las rutas de cada archivo
app.include_router(index)
app.include_router(obtener_equipos)
app.include_router(obtener_equipo)
app.include_router(agregar_equipo)
