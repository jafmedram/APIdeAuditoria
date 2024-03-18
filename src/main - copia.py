from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text
from uuid import uuid4 as uuid


app = FastAPI()

posts = []

class Equipo(BaseModel):
    idEquipo: str
    nombre: Text
    entrenador: Text
    capitan: Text
    liga: Text


@app.get("/")
def inicio():
    return {"Hola Mundo": "Hello World"}

@app.get("/equipos")
def mostrar_equipos():
    return posts

@app.post("/equipos")
def guardar_equipos(equipo: Equipo):
    Equipo.id = str(uuid())
    posts.append(equipo.dict())
    return posts[-1]

@app.get("/equipos/{idEquipo}")
def get_equipo(idEquipo: str):
    return {"idEquipo": idEquipo}
