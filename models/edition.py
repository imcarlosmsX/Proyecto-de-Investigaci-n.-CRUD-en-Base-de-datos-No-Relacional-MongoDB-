from typing import Optional
from pydantic import BaseModel
from books import Libro

class Edicion(BaseModel):
    
    isbn: str
    year: str
    idioma: str
    titulo_libro: str