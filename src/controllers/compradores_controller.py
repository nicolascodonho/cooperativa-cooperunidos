import random
from fastapi import HTTPException
from sqlalchemy.orm import Session
import src.models.schemas as schemas, src.models.models as models

def create_data(db: Session, comprador: schemas.CompradoresCreate):
    data = models.Compradores(**comprador.dict())
    data.id = random.getrandbits(32)
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def get_all_data(db: Session, skip: int = 0, limit: int = 10):
    data = db.query(models.Compradores).offset(skip).limit(limit).all()
    if not data:
        raise HTTPException(404, detail="Id nao encontrado")
    return data

def get_id_data(id: int, db: Session):
    return db.query(models.Compradores).filter(models.Compradores.id == id).first()

def delete_by_id(id: int, db: Session):
    return db.query(models.Compradores).filter(models.Compradores.id == id).delete()

def update_data(id: int, db: Session, compradores: schemas.CompradoresUpdate):
    db_comprador = db.query(models.Compradores).filter(models.Compradores.id == id).first()
    db_comprador.nome_empresa = compradores.nome_empresa
    db.commit()
    db.refresh(db_comprador)
    return db_comprador