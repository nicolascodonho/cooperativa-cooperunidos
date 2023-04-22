from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from src.models import schemas, models
from src.database.get_db import get_db
from src.database.connection import engine
from src.controllers import vendas_controller 

router = APIRouter(
    tags=["Vendas"]
)

models.Base.metadata.create_all(bind=engine)

@router.get("/busca")
def get_vendas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):

    vendas = vendas_controller.get_all_data(db, skip, limit)
    if not vendas:
        return HTTPException(404, detail="Lista de vendas vazias!")
    return vendas, 200

@router.get("/busca/{id}")
def get_venda(id: int, db: Session = Depends(get_db)):
    venda = vendas_controller.get_id_data(id, db)
    return venda, 200

@router.post("/cria")
async def save_venda(vendas: schemas.VendasCreate, db: Session = Depends(get_db)):
    try:
        vendas_controller.create_data(db, vendas)
        return "Dados criados com sucesso", 201
    except Exception as e:
        return HTTPException(500, detail="Nao foi possível criar dados, erro interno")

@router.put("/atualiza/{id}")
async def update_venda(id: int, venda: schemas.VendasUpdate, db: Session = Depends(get_db)):
    
    vendas_controller.get_id_data(id, db)
    
    try:
        vendas_controller.update_data(id, db, venda)
        return "Dados atualizados com sucesso", 204
    except Exception as e:
        return HTTPException(500, detail="Nao foi possivel atualizar dados, erro interno")
    
@router.delete("/deleta/{id}")
async def delete_venda(id: int, db: Session = Depends(get_db)):

    vendas_controller.get_id_data(id, db)

    try:
        vendas_controller.delete_by_id(id, db)
        msg = "Dados excluídos com sucesso"
        return msg, 200
    except Exception as e:
        return HTTPException(500, detail="Nao foi possivel deletar dados, erro interno")