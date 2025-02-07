from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.materials
import schemas.materials
from config.db import SessionLocal

router = APIRouter()


def get_db():
    """
    Función que proporciona una sesión de base de datos.
    Se utiliza como dependencia para las rutas que requieren acceso a la base de datos.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/materials/", response_model=List[schemas.materials.Material], tags=["Materiales"]
)
def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Recupera una lista de materiales desde la base de datos.
    Se puede especificar un desplazamiento (skip) y un límite en la cantidad de materiales.
    """
    materials = crud.materials.get_materials(db, skip=skip, limit=limit)
    return materials


@router.get(
    "/materials/{material_id}",
    response_model=schemas.materials.Material,
    tags=["Materiales"],
)
def read_material(material_id: int, db: Session = Depends(get_db)):
    """
    Recupera un material específico desde la base de datos usando su ID.
    Si el material no existe, se lanza una excepción HTTP 404.
    """
    db_material = crud.materials.get_material(db, material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material


@router.post(
    "/materials/", response_model=schemas.materials.Material, tags=["Materiales"]
)
def create_material(
    material: schemas.materials.MaterialCreate, db: Session = Depends(get_db)
):
    """
    Crea un nuevo material en la base de datos.
    """
    return crud.materials.create_material(db=db, material=material)


@router.put(
    "/materials/{material_id}",
    response_model=schemas.materials.Material,
    tags=["Materiales"],
)
def update_material(
    material_id: int,
    material: schemas.materials.MaterialUpdate,
    db: Session = Depends(get_db),
):
    """
    Actualiza un material existente en la base de datos usando su ID.
    Si el material no existe, se lanza una excepción HTTP 404.
    """
    db_material = crud.materials.get_material(db, material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return crud.materials.update_material(db=db, id=material_id, material=material)


@router.delete(
    "/materials/{material_id}",
    response_model=schemas.materials.Material,
    tags=["Materiales"],
)
def delete_material(material_id: int, db: Session = Depends(get_db)):
    """
    Elimina un material de la base de datos usando su ID.
    Si el material no existe, se lanza una excepción HTTP 404.
    """
    db_material = crud.materials.get_material(db, material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return crud.materials.delete_material(db=db, id=material_id)
