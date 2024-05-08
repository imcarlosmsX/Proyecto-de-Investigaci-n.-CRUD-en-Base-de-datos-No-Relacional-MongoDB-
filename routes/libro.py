from fastapi import APIRouter
from config.db import conn
from models.books import Libro
from schemas.books import bookEntity
from pymongo import ReturnDocument

libro = APIRouter()

#crear libro
@libro.post('/createlibreria')
def create_libro(libro: Libro):
    new_libro = dict(libro)
    id = conn.libreria.libro.insert_one(new_libro).inserted_id
    libro = conn.libreria.libro.find_one({'_id': id})
    return str((libro))

#actualizar libro
@libro.put('/updatelibro/{titulo_libro}')
def update_libro(nombre_libro: str, libro: Libro):
    new_libro = conn.libreria.libro.find_one_and_update({'titulo_libro': nombre_libro}, {'$set': dict(libro)}, return_document=ReturnDocument.AFTER)
    return str(bookEntity(new_libro))

#eliminar libro
@libro.delete('/deletelibro/{titulo_libro}')
def delete_libro(nombre_libro: str):
    conn.libreria.libro.find_one_and_delete({'titulo_libro': nombre_libro})
    return "Book deleted successfully"