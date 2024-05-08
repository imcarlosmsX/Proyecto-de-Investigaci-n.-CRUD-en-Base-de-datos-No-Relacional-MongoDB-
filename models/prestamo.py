from typing import Optional
from pydantic import BaseModel


class Prestamo(BaseModel):
    fecha_prestamo: str
    fecha_devolucion: str
    rut: str
    numero_copia: str
    isbn: str