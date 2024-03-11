from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4 as uuid


app = FastAPI()

class Equipo(BaseModel):
    idEquipo: str
    nombre: str
    entrenador: str
    capitan: str
    liga: str

equipos = []

@app.get("/")
def inicio():
    return {"Hola Mundo": "Hello World"}

@app.get("/equipos", response_model=List[Equipo])
def mostrar_equipos():
    return equipos

@app.post("/equipos", response_model=Equipo)
def guardar_equipo(equipo: Equipo):
    equipo.idEquipo = str(uuid())
    equipos.append(equipo)
    return equipo

@app.get("/equipos/{idEquipo}", response_model=Equipo)
def get_equipo(idEquipo: str):
    for equipo in equipos:
        if equipo.idEquipo == idEquipo:
            return equipo
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

@app.put("/equipos/{idEquipo}", response_model=Equipo)
def actualizar_equipo(idEquipo: str, equipo_nuevo: Equipo):
    for i, equipo in enumerate(equipos):
        if equipo.idEquipo == idEquipo:
            equipos[i] = equipo_nuevo
            return equipo_nuevo
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

@app.delete("/equipos/{idEquipo}")
def eliminar_equipo(idEquipo: str):
    for i, equipo in enumerate(equipos):
        if equipo.idEquipo == idEquipo:
            del equipos[i]
            return {"mensaje": "Equipo eliminado"}
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

