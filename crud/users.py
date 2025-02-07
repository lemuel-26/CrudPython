import models.users
import schemas.users
from sqlalchemy.orm import Session

# funciones CRUD para la tabla de usuarios
def get_user(db: Session, id: int):
    """
    Obtiene un usuario de la base de datos por su ID.

    Args:
        db (Session): Sesión de la base de datos.
        user_id (int): ID del usuario.

    Returns:
        User: Usuario con el ID especificado, o None si no existe.
    """
    return db.query(models.users.User).filter(models.users.User.id == id).first()

# Función para obtener una lista de usuarios con paginación
def get_users(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene una lista de usuarios de la base de datos con paginación.

    Args:
        db (Session): Sesión de la base de datos.
        skip (int): Número de registros a omitir (paginación).
        limit (int): Número máximo de registros a retornar.

    Returns:
        list: Lista de usuarios.
    """
    return db.query(models.users.User).offset(skip).limit(limit).all()

# Función para crear un nuevo usuario
def create_user(db: Session, user: schemas.users.UserCreate):
    """
    Crea un nuevo usuario en la base de datos.

    Args:
        db (Session): Sesión de la base de datos.
        user (UserCreate): Datos del nuevo usuario a crear.

    Returns:
        User: El usuario creado.
    """
    db_user = models.users.User(
        nombre=user.nombre,
        primerApellido=user.primerApellido,
        segundoApellido=user.segundoApellido,
        tipoUsuario=user.tipoUsuario,
        nombreUsuario=user.nombreUsuario,
        correoElectronico=user.correoElectronico,
        contrasena=user.contrasena,
        numeroTelefono=user.numeroTelefono,
        estatus=user.estatus,
        fechaRegistro=user.fechaRegistro,
        fechaActualizacion=user.fechaActualizacion,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Función para actualizar un usuario existente
def update_user(db: Session, id: int, user: schemas.users.UserUpdate):
    """
    Actualiza los datos de un usuario en la base de datos.

    Args:
        db (Session): Sesión de la base de datos.
        user_id (int): ID del usuario a actualizar.
        user (UserUpdate): Nuevos datos del usuario.

    Returns:
        User: El usuario actualizado.
    """
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
    if db_user:
        update_data = user.dict(exclude_unset=True)  # Excluir campos no establecidos
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user


# Función para eliminar un usuario
def delete_user(db: Session, user_id: int):
    """
    Elimina un usuario de la base de datos.

    Args:
        db (Session): Sesión de la base de datos.
        user_id (int): ID del usuario a eliminar.

    Returns:
        User: El usuario eliminado.
    """
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Función para obtener un usuario por su nombre de usuario
def get_user_by_usuario(db: Session, usuario: str):
    """
    Obtiene un usuario de la base de datos por su nombre de usuario.

    Args:
        db (Session): Sesión de la base de datos.
        usuario (str): Nombre de usuario.

    Returns:
        User: Usuario con el nombre de usuario especificado, o None si no existe.
    """
    return db.query(models.users.User).filter(models.users.User.nombreUsuario == usuario).first()
