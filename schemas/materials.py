from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

# Definir los tipos posibles de materiales
class TipoMaterial(str, Enum):
    """
    Enum que define los posibles tipos de materiales.
    """
    Canon = "Canon"
    Computadora = "Computadora"
    Extension = "Extension"

# Definir los estados posibles de un material
class EstadoMaterial(str, Enum):
    """
    Enum que define los posibles estados de un material.
    """
    Disponible = "Disponible"
    Prestado = "Prestado"
    EnMantenimiento = "En Mantenimiento"

# Esquema base para los materiales
class MaterialBase(BaseModel):
    """
    Esquema base para un material, utilizado para la creación y actualización.
    """
    tipoMaterial: TipoMaterial
    marca: str
    modelo: str
    estado: EstadoMaterial

# Esquema para la creación de un material
class MaterialCreate(MaterialBase):
    """
    Esquema para crear un nuevo material.
    """
    pass

# Esquema para la actualización de un material
class MaterialUpdate(BaseModel):
    """
    Esquema para actualizar los campos de un material.
    """
    tipoMaterial: Optional[TipoMaterial] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    estado: Optional[EstadoMaterial] = None

# Esquema para representar un material con todos los campos, incluyendo el ID
class Material(MaterialBase):
    """
    Representación completa de un material, con el ID.
    """
    id: int
    class Config:
        from_attributes = True
