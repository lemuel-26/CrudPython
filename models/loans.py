from sqlalchemy import Column, Integer, DateTime, Enum
from config.db import Base
import enum
# Enum que representa los posibles estados de un préstamo
class EstadoPrestamo(str, enum.Enum):
    """
    Enum que define los estados posibles de un préstamo.
    """
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

class Prestamo(Base):
    """
    Clase que representa la entidad Prestamo en la base de datos.
    """
    __tablename__ = "tbb_loans"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer)  # ForeignKey("tbb_users.id")
    idMaterial = Column(Integer)  # ForeignKey("tbb_materials.id")
    fechaPrestamo = Column(DateTime)
    fechaDevolucion = Column(DateTime)
    estadoPrestamo = Column(Enum(EstadoPrestamo))
