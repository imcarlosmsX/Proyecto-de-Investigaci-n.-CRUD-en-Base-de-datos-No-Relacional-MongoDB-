from fastapi import APIRouter
from config.db import conn
from schemas.users import *
from schemas.books import *
from schemas.edition import *
from schemas.copys import *
from schemas.prestamo import *

from models.books import *
from models.edition import *
from models.copys import *
from models.users import *
from models.prestamo import *
from models.author import *

from passlib.hash import sha256_crypt
from bson import ObjectId

user = APIRouter()

#crear autor
@user.post('/creatheautor', response_model=list[User])
def create_author(autor: Autor):
    new_author = dict(autor)
    id = conn.local.author.insert_one(new_author).inserted_id
    author = conn.local.author.find_one({'_id': id})
    return authorEntity(author)

#actualizar autor
@user.put('/updateautor/{id}', response_model=list[User])
def update_author(id: str, autor: Autor):
    conn.local.author.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(autor)})
    return authorEntity(conn.local.author.find_one({'_id': ObjectId(id)}))

#eliminar autor
@user.delete('/deleteautor/{id}', response_model=list[User])
def delete_author(id: str):
    authorEntity(conn.local.author.find_one_and_delete({'_id': ObjectId(id)}))
    return "Author deleted successfully"


#crear libro
@user.post('/creathelibro', response_model=list[User])
def create_book(libro: Libro):
    new_book = dict(libro)
    id = conn.local.book.insert_one(new_book).inserted_id
    book = conn.local.book.find_one({'_id': id})
    return bookEntity(book)

#actualizar libro
@user.put('/updatelibro/{id}', response_model=list[User])
def update_book(id: str, libro: Libro):
    conn.local.book.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(libro)})
    return bookEntity(conn.local.book.find_one({'_id': ObjectId(id)}))

#eliminar libro
@user.delete('/deletelibro/{id}', response_model=list[User])
def delete_book(id: str):
    bookEntity(conn.local.book.find_one_and_delete({'_id': ObjectId(id)}))
    return "Book deleted successfully"

#crear edicion
@user.post('/creathedicion', response_model=list[User])
def create_edition(edicion: Edicion):
    new_edition = dict(edicion)
    id = conn.local.edition.insert_one(new_edition).inserted_id
    edition = conn.local.edition.find_one({'_id': id})
    return editionEntity(edition)

#actualizar edicion
@user.put('/updateedicion/{id}', response_model=list[User])
def update_edition(id: str, edicion: Edicion):
    conn.local.edition.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(edicion)})
    return editionEntity(conn.local.edition.find_one({'_id': ObjectId(id)}))

#eliminar edicion
@user.delete('/deleteedicion/{id}', response_model=list[User])
def delete_edition(id: str):
    editionEntity(conn.local.edition.find_one_and_delete({'_id': ObjectId(id)}))
    return "Edition deleted successfully"

#crear copia
@user.post('/creathcopia', response_model=list[User])
def create_copy(copia: Copia):
    new_copy = dict(copia)
    id = conn.local.copy.insert_one(new_copy).inserted_id
    copy = conn.local.copy.find_one({'_id': id})
    return copyEntity(copy)

#actualizar copia
@user.put('/updatecopia/{id}', response_model=list[User])
def update_copy(id: str, copia: Copia):
    conn.local.copy.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(copia)})
    return copyEntity(conn.local.copy.find_one({'_id': ObjectId(id)}))

#eliminar copia
@user.delete('/deletecopia/{id}', response_model=list[User])
def delete_copy(id: str):
    copyEntity(conn.local.copy.find_one_and_delete({'_id': ObjectId(id)}))
    return "Copy deleted successfully"

#crear usuario
@user.post('/creatheuser', response_model=list[User])
def create_user(user: User):
    new_user = dict(user)
    new_user['password'] = sha256_crypt.encrypt(new_user['password'])
    id = conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({'_id': id})
    return userEntity(user)

#actualizar usuario
@user.put('/updateuser/{id}', response_model=list[User])
def update_user(id: str, user: User):
    conn.local.user.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(user)})
    return userEntity(conn.local.user.find_one({'_id': ObjectId(id)}))

#eliminar usuario
@user.delete('/deleteuser/{id}', response_model=list[User])
def delete_user(id: str):
    userEntity(conn.local.user.find_one_and_delete({'_id': ObjectId(id)}))
    return "User deleted successfully"

#crear prestamo
@user.post('/creathprestamo', response_model=list[User])
def create_loan(prestamo: Prestamo):
    new_loan = dict(prestamo)
    id = conn.local.loan.insert_one(new_loan).inserted_id
    loan = conn.local.loan.find_one({'_id': id})
    return loansEntity(loan)

#actualizar prestamo
@user.put('/updateprestamo/{id}', response_model=list[User])
def update_loan(id: str, prestamo: Prestamo):
    conn.local.loan.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(prestamo)})
    return loansEntity(conn.local.loan.find_one({'_id': ObjectId(id)}))

#eliminar prestamo
@user.delete('/deleteprestamo/{id}', response_model=list[User])
def delete_loan(id: str):
    loansEntity(conn.local.loan.find_one_and_delete({'_id': ObjectId(id)}))
    return "Loan deleted successfully"


@user.get('/user', response_model=list[User])
def find_all_users():
    return usersEntity(conn.local.user.find())

@user.post('/users')
def create_users(user: User):
    new_user = dict(user)
    new_user['password'] = sha256_crypt.encrypt(new_user['password'])
    id = conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({'_id': id})
    return userEntity(user)


@user.get('/find/{id}')
def find_user(id: str):
    return userEntity(conn.local.user.find_one({'_id': ObjectId(id)}))

@user.put('/update/{id}')
def update_user(id: str, user: User):
    conn.local.user.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(user)})
    return userEntity(conn.local.user.find_one({'_id': ObjectId(id)}))

@user.delete('/user/{id}')
def delete_user(id: str):
    userEntity(conn.local.user.find_one_and_delete({'_id': ObjectId(id)}))
    return "User deleted successfully"