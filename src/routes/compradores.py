from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from src.models import schemas, models
from src.database.get_db import get_db
from src.database.connection import engine
from src.controllers import compradores_controller
from src.configs.util import get_current_user

router = APIRouter(
    tags=["Compradores"]
)

models.Base.metadata.create_all(bind=engine)


@router.get("/busca")
def get_compradores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user = Depends(get_current_user)):
    """
    <code class='highlight'>/busca</code>
        Retorna os compradores existentes dentro do banco limitados por skip e limit"""

    compradores = compradores_controller.get_all_data(db, skip, limit)
    if not compradores:
        return HTTPException(404, detail="Lista de compradores vazias!")
    return {
        "mensagem": compradores,
        "status": 200
    }

@router.get("/busca/{id}")
def get_comprador(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    """
    <code class='highlight'>/busca/{id}</code>
        Retorna o comprador através de um ID"""
    comprador = compradores_controller.get_id_data(id, db)
    return {
        "mensagem": comprador,
        "status": 200
    }

@router.post("/cria")
async def save_compradores(compradores: schemas.CompradoresCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    """
    <code class='highlight'>/cria</code>
        Cria compradores baseado nos models """
    try:
        compradores_controller.create_data(db, compradores)
        return {
            "mensagem": "Dados criados com sucesso",
            "status": 201
        }        

    except Exception as e:
        return HTTPException(500, detail="Nao foi possível criar dados, erro interno")

@router.put("/atualiza/{id}")
async def update_comprador(id: int, comprador: schemas.CompradoresUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    """
    <code class='highlight'>/atualiza/{id}</code>
        Atualiza dados através de um ID"""
    compradores_controller.get_id_data(id, db)
    
    try:
        compradores_controller.update_data(id, db, comprador)
        return {
            "mensagem": "Dados atualizados com sucesso",
            "status": 204
        }
    except Exception as e:
        return HTTPException(500, detail="Nao foi possivel atualizar dados, erro interno")
    
@router.delete("/deleta/{id}")
async def delete_comprador(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    """
    <code class='highlight'>/delete/{id}</code>
        Deleta dados através de um ID"""
    compradores_controller.get_id_data(id, db)

    try:
        compradores_controller.delete_by_id(id, db)
        msg = "Dados excluídos com sucesso"
        return {
            "mensagem": msg,
            "status": 204
        }
    except Exception as e:
        return HTTPException(500, detail="Nao foi possivel deletar dados, erro interno")