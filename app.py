from fastapi import FastAPI

from routes.usuario import user 
from routes.autor import autor
from routes.libro import libro
from routes.edicion import edicion
from routes.copia import copia
from routes.prestamo import loans
from routes.query1 import query


app = FastAPI()
app.include_router(user)
app.include_router(autor)
app.include_router(libro)
app.include_router(edicion)
app.include_router(copia)
app.include_router(loans)
app.include_router(query)
