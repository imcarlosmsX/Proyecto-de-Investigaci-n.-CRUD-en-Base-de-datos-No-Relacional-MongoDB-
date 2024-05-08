
from pydantic import BaseModel


class Autorea(BaseModel):
    titulo_libro: str
    nombre_autor: str
