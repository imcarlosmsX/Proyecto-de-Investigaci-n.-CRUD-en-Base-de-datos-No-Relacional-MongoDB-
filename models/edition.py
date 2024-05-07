from typing import Optional
from pydantic import BaseModel
from books import Libro

class Edicion(BaseModel):
    _id: Optional[str]
    ISBN: str
    ano: int
    idioma: str
    libro: Libro