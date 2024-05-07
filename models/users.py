from pydantic import BaseModel

class User(BaseModel):
    RUT: str
    nombre: str
    numero_copia: str
