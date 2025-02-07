from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base
import enum

# Módulo que define el modelo de usuario en la base de datos.

# Enum que representa los posibles tipos de usuario
class TipoUsuario(str, enum.Enum):
    """
    Enum que define los tipos de usuario disponibles.
    """
    Alumno = "Alumno"
    Profesor = "Profesor"
    Secretaria = "Secretaria"
    Laboratorista = "Laboratorista"
    Director = "Director"
    Administrativo = "Administrativo"

# Enum que representa los posibles estados de un usuario
class Estatus(str, enum.Enum):
    """
    Enum que define los estados posibles de un usuario.
    """
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"
    
class User(Base):
    """
    Clase que representa la entidad Usuario en la base de datos.
    Esta clase mapea la tabla 'tbb_users' que contiene información sobre los usuarios.
    """
    __tablename__ = "tbb_users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(60))
    primerApellido = Column(String(60))
    segundoApellido = Column(String(60))
    tipoUsuario = Column(Enum(TipoUsuario))
    nombreUsuario = Column(String(60))
    correoElectronico = Column(String(100))
    contrasena = Column(String(100))
    numeroTelefono = Column(String(20))
    estatus = Column(Enum(Estatus))
    fechaRegistro = Column(DateTime)
    fechaActualizacion = Column(DateTime)

