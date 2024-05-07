from typing import Optional
from pydantic import BaseModel
from books import Libro

class Autor(BaseModel):
    nombre: str
    titulo_libro: str