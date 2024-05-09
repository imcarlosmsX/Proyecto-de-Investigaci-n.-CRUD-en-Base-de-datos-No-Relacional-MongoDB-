
from pydantic import BaseModel


class Autorea(BaseModel):
    titulo_libro_autorea: str
    nombre_autor_autorea: str
