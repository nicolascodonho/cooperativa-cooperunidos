import random, json
from fastapi import HTTPException
from sqlalchemy.orm import Session
import src.models.schemas as schemas, src.models.models as models

def nome_insumo(id_insumo, db: Session):
    res_insumo = db.query(models.Insumos).filter(models.Insumos.id == id_insumo).first()
    return res_insumo.nome_insumo

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
        raise HTTPException(404, detail="Lista de vendas vazia!")
    return data

def get_vendas_parsed(date, db: Session, skip: int = 0, limit: int = 10):
    data =  db.query(models.Vendas).offset(skip).limit(limit).all()
    data_arr= []
    data_parsed = {}
    for venda in data:
        try:
            insumo = nome_insumo(venda.id_insumo, db)
            if str(venda.data_venda) == str(date):
                pesos = venda.peso
                total = venda.valor
                data_parsed = {
                    venda.data_venda:{
                        'peso': pesos,
                        'total': total,
                        'insumo': insumo
                    }
                }
            data_arr.append(data_parsed)
        except IndexError:
            break

    date_insumo_map = {}
    for entry in data_arr:
        for date, info in entry.items():
            peso = info["peso"]
            total = info["total"]
            insumo = info["insumo"]
            
            if date in date_insumo_map:
                if insumo in date_insumo_map[date]:
                    date_insumo_map[date][insumo]["peso"] += peso
                    date_insumo_map[date][insumo]["total"] += total
                else:
                    date_insumo_map[date][insumo] = {"peso": peso, "total": total}
            else:
                date_insumo_map[date] = {insumo: {"peso": peso, "total": total}}

    return date_insumo_map

def get_id_data(id: int, db: Session):
    return db.query(models.Vendas).filter(models.Vendas.id == id).first()

def delete_by_id(id: int, db: Session):
    existing_job = db.query(models.Vendas).filter(models.Vendas.id == id).first()
    if not existing_job:
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