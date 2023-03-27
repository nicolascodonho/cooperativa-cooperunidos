from fastapi import FastAPI, status, Depends
from pydantic import BaseModel
from datetime import datetime
import logging
from connection import engine, SessionLocal
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DATE
from sqlalchemy.orm import Session
import models, schemas, insumos_controller

dns = "127.0.0.1"
port = "8000"

app = FastAPI()

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {
        "message": "Olá, essa é a pagina inicial da api. Para visualizar as rotas existentes na mesma, utilize a rota /docs.",
        "link": f"{dns}:{port}/docs"
    }

@app.get("/busca", response_model = list[schemas.Insumos])
def get_insumos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    insumos = insumos_controller.get_all_data(db, skip, limit)
    
    return insumos, 200

@app.get("/busca/{id}")
def get_id_data():
    return {
        "message": "data"
    }

@app.post("/cria", response_model=schemas.Insumos)
def save(insumos: schemas.Insumos, db: Session = Depends(get_db)):
    try:
        data = insumos_controller.create_data(db, insumos)
        return data, 200
    except Exception as e:
        print(e)

@app.put("/atualiza/{id}")
def update_data():
    return {

    }

@app.delete("/delete/{id}")
def delete_by_id():
    return {

    }