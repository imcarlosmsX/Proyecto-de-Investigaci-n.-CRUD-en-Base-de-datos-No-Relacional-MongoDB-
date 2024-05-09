
from pymongo import MongoClient
from fastapi import APIRouter, Response, status
from config.db import conn

query = APIRouter()

CONSULTA1 = [
    {
        '$lookup': {
            'from': "autorea",
            'localField': "nombre_autor",
            'foreignField': "nombre_autor_autorea",
            'as': "autorea_1"
        }
    },
    {
        '$lookup': {
            'from': "libro",
            'localField': "autorea_1.titulo_libro_autorea",
            'foreignField': "titulo_libro",
            'as': "libro_1"
        }
    },
    {
        '$lookup': {
            'from': "edicion",
            'localField': "libro_1.isbn_editorial",
            'foreignField': "isbn",
            'as': "edicion_1"
        }
    },
    {
        '$lookup': {
            'from': "copia",
            'localField': "edicion_1.isbn",
            'foreignField': "isbn_editorial",
            'as': "copia_1"
        }   
    },
    {
        '$project': {
            '_id': 0,
            'nombre_autor': 1,
            "libro_1.titulo_libro":1,
            'edicion_1.isbn': 1,
            'edicion_1.year': 1,
            'edicion_1.idioma': 1,
            'copia_1.numero_copia': 1
        }
    }
]


CONSULTA2 = [
    {
        '$lookup': {
            'from': 'edicion',
            'localField': 'isbn_editorial',
            'foreignField': 'isbn',
            'as': 'edicion_1'
        }
    },
    {
        '$lookup': {
            'from': 'copia',
            'localField': 'edicion_1.isbn',
            'foreignField': 'isbn_editorial',
            'as': 'copia_1'
        }
    },
    {
        '$lookup': {
            'from': 'prestamo',
            'localField': 'copia_1.numero_copia',
            'foreignField': 'numero_copia_libro',
            'as': 'prestamo_1'
        }
    },
    {
        '$lookup':{
            'from': 'user',
            'localField': 'prestamo_1.rut_usuario',
            'foreignField':'rut',
            'as':'usuario'
        }
    },

    {
        '$match':{
            "usuario.rut": ""
        }   
    },
    {
        '$project': {
            "_id": 0,
            "titulo_libro": 1,
            
        }
    }
]
@query.get("/Query1/")
def get_copias():
    return list(conn.libreria.autor.aggregate(CONSULTA1))

@query.get("/Query2/{RUT}")
def get_librosUser(RUT: str):
    CONSULTA2[4]['$match']['usuario.rut'] = RUT
    return list(conn.libreria.libro.aggregate(CONSULTA2))