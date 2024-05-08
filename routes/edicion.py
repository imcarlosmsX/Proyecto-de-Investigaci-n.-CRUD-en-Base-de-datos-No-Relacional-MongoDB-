from models.edition import Edicion
from schemas.edition import editionEntity
from fastapi import APIRouter
from config.db import conn
from pymongo import ReturnDocument


edicion = APIRouter()

#crear edicion
@edicion.post('/createedicion')
def create_edicion(edicion: Edicion):
    new_edicion = dict(edicion)
    id = conn.libreria.edicion.insert_one(new_edicion).inserted_id
    edicion = conn.libreria.edicion.find_one({'_id': id})
    return str(editionEntity(edicion))


#actualizar edicion
@edicion.put('/updateedicion/{isbn}')
def update_edicion(isbn: str, edicion: Edicion):
    new_edicion = conn.libreria.edicion.find_one_and_update({'isbn': isbn}, {'$set': dict(edicion)}, return_document=ReturnDocument.AFTER)
    return str(editionEntity(new_edicion))

#eliminar edicion
@edicion.delete('/deleteedicion/{isbn}')
def delete_edicion(isbn: str):
    conn.libreria.edicion.find_one_and_delete({'isbn': isbn})
    return "Edition deleted successfully"


