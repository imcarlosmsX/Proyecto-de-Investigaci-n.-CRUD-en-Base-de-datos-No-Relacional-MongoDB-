from typing import Optional
from pydantic import BaseModel
from edition import Edicion


class Copia(BaseModel):
    numero_copia: str
    isbn: str
