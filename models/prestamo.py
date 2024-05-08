from typing import Optional
from pydantic import BaseModel


class Prestamo(BaseModel):
    rut: str
    numero_copia: str
    isbn: str
    fecha_prestamo: str
    fecha_devolucion: str
    