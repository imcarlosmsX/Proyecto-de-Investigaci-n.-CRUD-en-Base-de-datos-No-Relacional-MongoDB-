from pydantic import BaseModel

class User(BaseModel):
    rut: str
    nombre: str
    numero_copia: str
