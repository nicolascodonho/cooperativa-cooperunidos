import random
from fastapi import HTTPException
from sqlalchemy.orm import Session
import src.models.schemas as schemas, src.models.models as models

def create_data(db: Session, insumos: schemas.InsumosCreate):
    data = models.Insumos(**insumos.dict())
    data.id = random.getrandbits(32)
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def get_all_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Insumos).offset(skip).limit(limit).all()

def get_id_data(id: int, db: Session):
    data = db.query(models.Insumos).filter(models.Insumos.id == id).first()
    if not data:
        raise HTTPException(404, detail="Id nao encontrado")
    return data

def delete_by_id(id: int, db: Session):
    return db.query(models.Insumos).filter(models.Insumos.id == id).delete()

def update_data(id: int, db: Session, insumo: schemas.InsumosUpdate):
    db_insumo = db.query(models.Insumos).filter(models.Insumos.id == id).first()
    db_insumo.id_fornecedor = insumo.id_fornecedor
    db_insumo.nome_insumo = insumo.nome_insumo
    db.commit()
    db.refresh(db_insumo)
    return db_insumo