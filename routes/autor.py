from fastapi import APIRouter
from config.db import conn
from models.author import Autor
from schemas.authors import authorEntity
from pymongo import ReturnDocument

autor = APIRouter()


#crear autor
@autor.post('/creatautor')
def create_autor(autor: Autor):
    new_autor = dict(autor)
    id = conn.libreria.autor.insert_one(new_autor).inserted_id
    autor = conn.libreria.autor.find_one({'_id': id})
    return str(authorEntity(autor))

#actualizar autor
@autor.put('/updateautor/{nombre_autor}')
def update_autor(nombre_autor: str, autor: Autor):
    new_autor = conn.libreria.autor.find_one_and_update({'nombre_autor': nombre_autor}, {'$set': dict(autor)}, return_document=ReturnDocument.AFTER)
    return str(authorEntity(new_autor))

#eliminar autor
@autor.delete('/deleteautor/{nombre_autor}')
def delete_autor(nombre_autor: str):
    conn.libreria.autor.find_one_and_delete({'nombre_autor': nombre_autor})
    return "Author deleted successfully"


