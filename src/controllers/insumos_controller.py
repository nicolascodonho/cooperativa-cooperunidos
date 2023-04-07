from sqlalchemy.orm import Session
import src.models.schemas as schemas, src.models.models as models
from fastapi import HTTPException

def create_data(db: Session, insumos: schemas.Insumos):
    data = models.Insumos(**insumos.dict())

    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def get_all_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Insumos).offset(skip).limit(limit).all()

def get_id_data(id: int, db: Session):
    return db.query(models.Insumos).filter(models.Insumos.id == id).first()

def delete_by_id(id: int, db: Session):
    return db.query(models.Insumos).filter(models.Insumos.id == id).delete()

def update_data(id: int, db: Session, insumos: schemas.Insumos):
    db_data = db.get(insumos, id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Insumo não encontrado")
    insumo = insumos.dict(exclude_unset=True)

    for key, value in insumo.items():
        setattr(db_data, key, value)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data