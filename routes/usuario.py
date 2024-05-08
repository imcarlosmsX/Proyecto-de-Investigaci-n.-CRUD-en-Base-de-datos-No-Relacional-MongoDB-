from fastapi import APIRouter
from config.db import conn
from models.users import User
from schemas.users import userEntity

user = APIRouter()

#crear usuario
@user.post('/creatheuser')
def create_user(user: User):
    new_user = dict(user)
    id = conn.libreria.user.insert_one(new_user).inserted_id
    user = conn.libreria.user.find_one({'_id': id})
    return str(userEntity(user))

#actualizar usuario
@user.put('/updateuser/{rut}')
def update_user(rut: str, user: User):
    new_user = conn.libreria.user.find_one_and_update({'rut': rut}, {'$set': dict(user)})
    return str(userEntity(new_user))


#eliminar usuario
@user.delete('/deleteuser/{rut}')
def delete_user(rut: str):
    conn.libreria.user.find_one_and_delete({'rut': rut})
    return "User deleted successfully"
