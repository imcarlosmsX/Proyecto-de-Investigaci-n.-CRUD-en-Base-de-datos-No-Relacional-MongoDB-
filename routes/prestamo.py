from models.prestamo import Prestamo
from schemas.prestamo import loanEntity
from fastapi import APIRouter
from config.db import conn
from pymongo import ReturnDocument

loans = APIRouter()

#crear prestamo
@loans.post('/createprestamo')
def create_prestamo(prestamo: Prestamo):
    new_prestamo = dict(prestamo)
    id = conn.libreria.prestamo.insert_one(new_prestamo).inserted_id
    prestamo = conn.libreria.prestamo.find_one({'_id': id})
    return str(loanEntity(prestamo))


#actualizar prestamo
@loans.put('/updateprestamo/{rut, isbn, numero_copia}')
def update_prestamo(rut: str, isbn: str, numero_copia: str, prestamo: Prestamo):
    query = {'rut': rut, 'isbn': isbn, 'numero_copia': numero_copia}
    update_fields = {'$set': dict(prestamo)}
    
    new_prestamo = conn.libreria.prestamo.find_one_and_update(
        query,
        update_fields,
        return_document=ReturnDocument.AFTER
    )
    
    if new_prestamo:
        return str(loanEntity(new_prestamo))
    else:
        return "Prestamo no encontrado"

#eliminar prestamo
@loans.delete('/deleteprestamo/{rut, isbn, numero_copia}')
def delete_prestamo(rut: str, isbn: str, numero_copia: str):
    conn.libreria.prestamo.find_one_and_delete({'rut': rut, 'isbn': isbn,'numero_copia': numero_copia})
    return "Loan deleted successfully"


