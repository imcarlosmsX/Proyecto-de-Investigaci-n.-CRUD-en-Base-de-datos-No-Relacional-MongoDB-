from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId

user = APIRouter()

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