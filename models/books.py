from typing import Optional
from pydantic import BaseModel

class Libro(BaseModel):
    titulo: str
    nombre_autor: str
    isbn: str
    
# Path: Proyecto-de-Investigaci-n.-CRUD-en-Base-de-datos-No-Relacional-MongoDB-/schemas/copys.py