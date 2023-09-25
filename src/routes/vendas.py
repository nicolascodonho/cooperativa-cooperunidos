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
    """
        <code class='highlight'>/busca</code>
            Retorna as vendas existentes dentro do banco limitados por skip e limit"""

    vendas = vendas_controller.get_all_data(db, skip, limit)
    if not vendas:
        return HTTPException(404, detail="Lista de vendas vazias!")
    return {"mensagem": vendas, "status": 200}

@router.get("/busca/{id}")
def get_venda(id: int, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/busca/{id}</code>
        Retorna uma venda através de um ID"""
    venda = vendas_controller.get_id_data(id, db)
    return {"mensagem": venda, "status": 200}

@router.post("/cria")
async def save_venda(vendas: schemas.VendasCreate, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/cria</code>
        Cria vendas baseado nos models """
    try:
        vendas_controller.create_data(db, vendas)
        return {"mensagem": vendas, "status": 201}
    except Exception as e:
        return HTTPException(500, detail="Nao foi possível criar dados, erro interno")

@router.put("/atualiza/{id}")
async def update_venda(id: int, venda: schemas.VendasUpdate, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/atualiza/{id}</code>
        Atualiza dados através de um ID"""
    vendas_controller.get_id_data(id, db)
    
    try:
        vendas_controller.update_data(id, db, venda)
        return {"mensagem": "Dados atualizados com sucesso", "status": 204}
    except Exception as e:
        return HTTPException(500, detail="Nao foi possivel atualizar dados, erro interno")
    
@router.delete("/deleta/{id}")
async def delete_venda(id: int, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/delete/{id}</code>
        Deleta dados através de um ID"""
    vendas = vendas_controller.get_id_data(id, db)
    if not vendas:
        raise HTTPException(status_code=404, detail="Vendas not found")

    try:
        vendas_controller.delete_by_id(id, db)
        msg = "Dados excluídos com sucesso"
        return {"mensagem": msg, "status": 204}
    
    except Exception as e:
        return HTTPException(500, detail="Nao foi possivel deletar dados, erro interno")