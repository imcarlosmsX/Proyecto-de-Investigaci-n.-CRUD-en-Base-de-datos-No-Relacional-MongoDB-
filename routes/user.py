from fastapi import APIRouter
from config.db import conn
from passlib.hash import sha256_crypt
from bson import ObjectId
from models.users import User
from schemas.users import userEntity

user = APIRouter()

#crear usuario
@user.post('/creatheuser', response_model=list[User])
def create_user(user: User):
    new_user = dict(user)
    id = conn.libreria.user.insert_one(new_user).inserted_id
    user = conn.libreria.user.find_one({'_id': id})
    return userEntity(user)

#actualizar usuario
@user.put('/updateuser/{rut}', response_model=list[User])
def update_user(rut: str, user: User):
    conn.libreria.user.find_one_and_update({rut: str}, {'$set': dict(user)})
    return userEntity(conn.libreria.user.find_one({rut: str}))

#eliminar usuario
@user.delete('/deleteuser/{rut}', response_model=list[User])
def delete_user(rut: str):
    userEntity(conn.libreria.user.find_one_and_delete({rut: str}))
    return "User deleted successfully"
