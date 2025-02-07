from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

# Definir los tipos posibles de usuarios
class TipoUsuario(str, Enum):
    """
    Enum que define los posibles tipos de usuarios.
    """
    Alumno = "Alumno"
    Profesor = "Profesor"
    Secretaria = "Secretaria"
    Laboratorista = "Laboratorista"
    Director = "Director"
    Administrativo = "Administrativo"

# Definir los posibles estados de un usuario
class Estatus(str, Enum):
    """
    Enum que define los posibles estatus de un usuario.
    """
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"

# Esquema base para un usuario
class UserBase(BaseModel):
    """
    Esquema base para un usuario, utilizado para la creación y actualización.
    """
    nombre: str
    primerApellido: str
    segundoApellido: str
    tipoUsuario: TipoUsuario
    nombreUsuario: str
    correoElectronico: str
    contrasena: str
    numeroTelefono: str
    estatus: Estatus
    fechaRegistro: datetime
    fechaActualizacion: datetime
    
# Esquema para la creación de un usuario
class UserCreate(UserBase):
    """
    Esquema para crear un nuevo usuario.
    """
    pass

# Esquema para la actualización de un usuario
class UserUpdate(BaseModel):
    """
    Esquema para actualizar los campos de un usuario.
    """
    nombre: Optional[str] = None
    primerApellido: Optional[str] = None
    segundoApellido: Optional[str] = None
    tipoUsuario: Optional[TipoUsuario] = None
    nombreUsuario: Optional[str] = None
    correoElectronico: Optional[str] = None
    contrasena: Optional[str] = None
    numeroTelefono: Optional[str] = None
    estatus: Optional[Estatus] = None
    fechaRegistro: Optional[datetime] = None
    fechaActualizacion: Optional[datetime] = None

# Esquema para representar un usuario con todos los campos, incluyendo el ID
class User(UserBase):
    """
    Representación completa de un usuario, con el ID.
    """
    id: int
    class Config:
        from_attributes = True
