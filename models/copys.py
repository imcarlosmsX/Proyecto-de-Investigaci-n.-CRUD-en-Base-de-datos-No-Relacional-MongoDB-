from typing import Optional
from pydantic import BaseModel
from edition import Edicion


class Copia(BaseModel):
    _id: Optional[str]
    numero: int
    isbn: str