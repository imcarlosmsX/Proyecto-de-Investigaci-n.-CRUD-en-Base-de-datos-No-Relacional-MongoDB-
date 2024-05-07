from typing import Optional
from pydantic import BaseModel

class Libro(BaseModel):
    isbn: str
    titulo: str
    autor_nombre: str
    year: int
    idioma: str
    
# Path: Proyecto-de-Investigaci-n.-CRUD-en-Base-de-datos-No-Relacional-MongoDB-/schemas/copys.py