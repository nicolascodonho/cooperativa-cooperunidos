import random
from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
import src.models.schemas as schemas, src.models.models as models
from src.configs.util import get_hashed_password

def get_user_by_email(db: Session, email: EmailStr):
    data = db.query(models.Usuarios).filter(models.Usuarios.email == email).first()
    if not data:
        raise HTTPException(404, detail="Usuário não encontrado!")
    return data


def create_data(db: Session, usuarios: schemas.UsuariosCreate):
    data = models.Usuarios(**usuarios.dict())
    data.id = random.getrandbits(32)
    data.password = get_hashed_password(data.password)
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def delete_by_id(id: int, db: Session):
    existing_job = db.query(models.Usuarios).filter(models.Usuarios.id == id).first()
    if not existing_job:
        return 0
    db.delete(existing_job)
    db.commit()
    return existing_job

def update_data(id: int, db: Session, usuarios: schemas.UsuariosUpdate):
    db_Usuarios = db.query(models.Usuarios).filter(models.Usuarios.id == id).first()
    db_Usuarios.empresa = usuarios.empresa
    db_Usuarios.nome = usuarios.nome
    db.commit()
    db.refresh(db_Usuarios)
    return db_Usuarios
