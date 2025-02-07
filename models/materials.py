from sqlalchemy import Column, Integer, String, Enum
from config.db import Base
import enum
# Módulo que define los modelos de materiales en la base de datos.

# Enum que representa los tipos posibles de material
class TipoMaterial(str, enum.Enum):
    """
    Enum que define los tipos de material disponibles.
    """
    Canon = "Canon"
    Computadora = "Computadora"
    Extension = "Extension"

# Enum que representa los estados posibles de un material
class EstadoMaterial(str, enum.Enum):
    """
    Enum que define los estados posibles de un material.
    """
    Disponible = "Disponible"
    Prestado = "Prestado"
    EnMantenimiento = "En Mantenimiento"

class Material(Base):
    """
    Clase que representa la entidad Material en la base de datos.
    Esta clase mapea la tabla 'tbb_materials' que contiene información sobre los materiales.
    """
    __tablename__ = "tbb_materials"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipoMaterial = Column(Enum(TipoMaterial))
    marca = Column(String(60))
    modelo = Column(String(60))
    estado = Column(Enum(EstadoMaterial))
    # idUsuario = Column(Integer, ForeignKey("tbb_users.id"))
