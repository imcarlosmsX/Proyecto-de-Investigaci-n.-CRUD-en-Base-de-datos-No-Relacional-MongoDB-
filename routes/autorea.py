from fastapi import APIRouter
from config.db import conn
from models.autorea import Autorea
from schemas.autorea import autoreaEntity
from pymongo import ReturnDocument


autorea = APIRouter()

#create autorea
@autorea.post('/createautorea {autorea: Autorea}')
def create_edicion(autorea: Autorea):
    new_autorea = dict(autorea)
    id = conn.libreria.autorea.insert_one(new_autorea).inserted_id
    edicion = conn.libreria.autorea.find_one({'_id': id})
    return str(autoreaEntity(edicion))

#update autorea
@autorea.put('/updateautorea/{titulo_libro_autorea}')
def update_edicion(titulo_libro_autorea: str, nombre_autor_autorea: str, autorea: Autorea):
    new_autorea = conn.libreria.autorea.find_one_and_update({'titulo_libro_autorea': titulo_libro_autorea, 'nombre_autor_autorea': nombre_autor_autorea}, {'$set': dict(autorea)}, return_document=ReturnDocument.AFTER)
    return str(autoreaEntity(new_autorea))

#delete autorea
@autorea.delete('/deleteautorea/    {titulo_libro_autorea}')
def delete_autorea(titulo_libro_autorea: str, nombre_autor_autorea: str):
    conn.libreria.autorea.find_one_and_delete({'titulo_libro_autorea': titulo_libro_autorea, 'nombre_autor_autorea': nombre_autor_autorea})
    return "Se ha eliminado el autor del libro con titulo: " + titulo_libro_autorea + " y nombre: " + nombre_autor_autorea

