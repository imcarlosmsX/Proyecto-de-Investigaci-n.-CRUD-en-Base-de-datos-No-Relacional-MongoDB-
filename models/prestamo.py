from typing import Optional
from pydantic import BaseModel
from edition import Edicion

class Prestamo(BaseModel):
    fecha_prestamo: str
    fecha_devolucion: str
    edicion: Edicion