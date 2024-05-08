from typing import Optional
from pydantic import BaseModel


class Autor(BaseModel):
    nombre_autor: str
