from fastapi import FastAPI, Depends, HTTPException
import logging
from connection import SessionLocal
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

@app.get("/busca/{id}", response_model=schemas.Insumos)
def get_insumo(id: int, db: Session = Depends(get_db)):
    insumo = insumos_controller.get_id_data(db, id=id)
    if insumo is None:
        raise HTTPException(status_code=404, detail="Insumo não encontrado")
    return insumo, 200

@app.post("/cria", response_model=schemas.Insumos)
async def save(insumos: schemas.Insumos, db: Session = Depends(get_db)):
    try:
        data = await insumos_controller.create_data(db, insumos)
        return data, 200
    except Exception as e:
        print(e)

@app.put("/atualiza/{id}", response_model=schemas.Insumos)
def update_data(id: int, insumos: schemas.Insumos, db: Session = Depends(get_db)):
    try:
        data = insumos_controller.update_data(id, db, insumos)
        return data, 200
    except Exception as e:
        print(e)
    

@app.delete("/delete/{id}", response_model=schemas.Insumos)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = insumos_controller.delete_by_id(id, db)
        return data, 200
    except Exception as e:
        print(e)