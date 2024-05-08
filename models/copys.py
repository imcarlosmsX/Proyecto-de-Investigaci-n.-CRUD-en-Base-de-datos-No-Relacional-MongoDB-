from typing import Optional
from pydantic import BaseModel


class Copia(BaseModel):
    numero_copia: str
    isbn: str
