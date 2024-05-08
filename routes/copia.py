from models.copys import Copia
from schemas.copys import copyEntity
from fastapi import APIRouter
from config.db import conn
from pymongo import ReturnDocument


copia = APIRouter()

#crear copia
@copia.post('/createcopia')
def create_copia(numero_copia: Copia):
    new_copia = dict(numero_copia)
    id = conn.libreria.copia.insert_one(new_copia).inserted_id
    copia = conn.libreria.copia.find_one({'_id': id})
    return str(copyEntity(copia))

#actualizar copia
@copia.put('/updatecopia/{numero_copia}')
def update_copia(numero_copia: str, copia: Copia):
    new_copia = conn.libreria.copia.find_one_and_update({'numero_copia': numero_copia}, {'$set': dict(copia)}, return_document=ReturnDocument.AFTER)
    return str(copyEntity(new_copia))


#eliminar copia
@copia.delete('/deletecopia/{numero_copia}')
def delete_copia(numero_copia: str):
    conn.libreria.copia.find_one_and_delete({'numero_copia': numero_copia})
    return "Copy deleted successfully"
