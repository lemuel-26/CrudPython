from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

# Definir los posibles estados de un préstamo
class EstadoPrestamo(str, Enum):
    """
    Enum que define los posibles estados de un préstamo.
    """
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

# Esquema base para los préstamos
class PrestamoBase(BaseModel):
    """
    Esquema base para un préstamo, utilizado para la creación y actualización.
    """
    idUsuario: int
    idMaterial: int
    fechaPrestamo: datetime
    fechaDevolucion: datetime
    estadoPrestamo: EstadoPrestamo

# Esquema para la creación de un préstamo
class PrestamoCreate(PrestamoBase):
    """
    Esquema para crear un préstamo nuevo.
    """
    pass

# Esquema para la actualización de un préstamo
class PrestamoUpdate(BaseModel):
    """
    Esquema para actualizar los campos de un préstamo.
    """
    idUsuario: Optional[int] = None
    idMaterial: Optional[int] = None
    fechaPrestamo: Optional[datetime] = None
    fechaDevolucion: Optional[datetime] = None
    estadoPrestamo: Optional[EstadoPrestamo] = None

# Esquema para representar un préstamo con todos los campos, incluyendo el ID
class Prestamo(PrestamoBase):
    """
    Representación completa de un préstamo, con el ID.
    """
    id: int
    class Config:
        from_attributes = True
