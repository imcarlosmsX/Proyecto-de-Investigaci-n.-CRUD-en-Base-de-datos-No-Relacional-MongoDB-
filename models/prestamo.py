from typing import Optional
from pydantic import BaseModel


class Prestamo(BaseModel):
    rut_usuario: str
    numero_copia_libro: str
    isbn_editorial: str
    fecha_prestamo: str
    fecha_devolucion: str
    