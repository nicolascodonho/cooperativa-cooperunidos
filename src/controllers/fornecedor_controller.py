import random
from fastapi import HTTPException
from sqlalchemy.orm import Session
import src.models.schemas as schemas, src.models.models as models

def create_data(db: Session, fornecedores: schemas.FornecedorCreate):
    data = models.Fornecedor(**fornecedores.dict())
    data.id = random.getrandbits(32)
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def get_all_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Fornecedor).offset(skip).limit(limit).all()

def get_id_data(id: int, db: Session):
    data = db.query(models.Fornecedor).filter(models.Fornecedor.id == id).first()
    if not data:
        raise HTTPException(404, detail="Lista de fornecedores vazia!")
    return data

def delete_by_id(id: int, db: Session):
    existing_job = db.query(models.Fornecedor).filter(models.Fornecedor.id == id).first()
    if not existing_job:
        return "Fornecedor não encontrado"
    
    try:
        insumos = db.query(models.Insumos).filter(models.Insumos.id_fornecedor == id).all()
        if insumos:
            for insumo in insumos:
                db.delete(insumo)

        db.delete(existing_job)
        db.commit()
        return existing_job
    except Exception as e:
        print("Opsie: ", e)

def update_data(id: int, db: Session, fornecedor: schemas.FornecedorUpdate):
    db_fornecedor = db.query(models.Fornecedor).filter(models.Fornecedor.id == id).first()
    db_fornecedor.empresa = fornecedor.empresa
    db_fornecedor.nome = fornecedor.nome
    db.commit()
    db.refresh(db_fornecedor)
    return db_fornecedor
