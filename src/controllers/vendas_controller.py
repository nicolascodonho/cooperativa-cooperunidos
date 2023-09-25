import random
from fastapi import HTTPException
from sqlalchemy.orm import Session
import src.models.schemas as schemas, src.models.models as models

def create_data(db: Session, vendas: schemas.VendasCreate):
    data = models.Vendas(**vendas.dict())
    data.id = random.getrandbits(32)
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def get_all_data(db: Session, skip: int = 0, limit: int = 10):
    data =  db.query(models.Vendas).offset(skip).limit(limit).all()
    if not data:
        raise HTTPException(404, detail="Id nao encontrado")
    return data

def get_id_data(id: int, db: Session):
    return db.query(models.Vendas).filter(models.Vendas.id == id).first()

def delete_by_id(id: int, db: Session):
    existing_job = db.query(models.Vendas).filter(models.Vendas.id == id)
    if not existing_job.first():
        return 0
    db.delete(existing_job)
    db.commit()
    return existing_job

def update_data(id: int, db: Session, venda: schemas.VendasUpdate):
    db_venda = db.query(models.Vendas).filter(models.Vendas.id == id).first()
    db_venda.id_insumo = venda.id_insumo
    db_venda.id_comprador = venda.id_comprador
    db_venda.peso = venda.peso
    db_venda.data_venda = venda.data_venda
    db_venda.responsavel = venda.responsavel
    db_venda.valor = venda.valor
    db.commit()
    db.refresh(db_venda)
    return db_venda