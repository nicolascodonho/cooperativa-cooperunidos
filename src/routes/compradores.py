from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from src.models import schemas, models
from src.database.get_db import get_db
from src.database.connection import engine
from src.controllers import compradores_controller 

router = APIRouter(
    tags=["Compradores"]
)

models.Base.metadata.create_all(bind=engine)


@router.get("/busca")
def get_compradores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):

    compradores = compradores_controller.get_all_data(db, skip, limit)
    if not compradores:
        return HTTPException(404, detail="Lista de compradores vazias!")
    return compradores, 200

@router.get("/busca/{id}")
def get_comprador(id: int, db: Session = Depends(get_db)):
    comprador = compradores_controller.get_id_data(id, db)
    return comprador, 200

@router.post("/cria")
async def save_compradores(compradores: schemas.CompradoresCreate, db: Session = Depends(get_db)):
    try:
        compradores_controller.create_data(db, compradores)
        return "Dados criados com sucesso", 201
    except Exception as e:
        return HTTPException(500, detail="Nao foi possível criar dados, erro interno")

@router.put("/atualiza/{id}")
async def update_comprador(id: int, comprador: schemas.CompradoresUpdate, db: Session = Depends(get_db)):
    
    compradores_controller.get_id_data(id, db)
    
    try:
        compradores_controller.update_data(id, db, comprador)
        return "Dados atualizados com sucesso", 204
    except Exception as e:
        return HTTPException(500, detail="Nao foi possivel atualizar dados, erro interno")
    
@router.delete("/deleta/{id}")
async def delete_comprador(id: int, db: Session = Depends(get_db)):

    compradores_controller.get_id_data(id, db)

    try:
        compradores_controller.delete_by_id(id, db)
        msg = "Dados excluídos com sucesso"
        return msg, 200
    except Exception as e:
        return HTTPException(500, detail="Nao foi possivel deletar dados, erro interno")