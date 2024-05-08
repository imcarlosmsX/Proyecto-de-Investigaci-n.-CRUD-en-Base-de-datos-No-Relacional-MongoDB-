from typing import Optional
from pydantic import BaseModel

class Edicion(BaseModel):
    
    isbn: str
    year: str
    idioma: str
