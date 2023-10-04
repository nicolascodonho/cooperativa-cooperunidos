from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from src.controllers import insumos_controller
from src.models import schemas, models
from src.database.get_db import get_db
from src.database.connection import engine

router = APIRouter(
    tags=["Insumos"]
)

models.Base.metadata.create_all(bind=engine)

@router.get("/busca")
def get_insumos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/busca</code>
        Retorna os insumos existentes dentro do banco limitados por skip e limit"""
    insumos = insumos_controller.get_all_data(db, skip, limit)
    if not insumos:
          return HTTPException(404, detail="Lista de insumos vazios!")
    return {"mensagem": insumos, "status": 200}

@router.get("/busca/{id}")
def get_insumo(id: int, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/busca/{id}</code>
        Retorna o insumo através de um ID"""
    insumo = insumos_controller.get_id_data(id, db)
    return {"mensagem": insumo, "status": 200}

@router.post("/cria")
async def save_insumos(insumos: schemas.InsumosCreate, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/cria</code>
        Cria insumos baseado nos models """
    try:
        insumos_controller.create_data(db, insumos)
        msg = "Dados criados com sucesso"
        return {"mensagem": msg, "status": 201}
    except Exception as e:
        return HTTPException(500, detail="Nao foi possivel criado insumo, erro interno")

@router.put("/atualiza/{id}")
async def update_insumos(id: int, insumos: schemas.InsumosUpdate, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/atualiza/{id}</code>
        Atualiza dados através de um ID"""
    
    insumos_controller.get_id_data(id, db)

    try:
        insumos_controller.update_data(id, db, insumos)
        msg = "Dados atualizados com sucesso"
        return {"mensagem": msg, "status": 204}
    except Exception as e:
        return HTTPException(500, detail="Nao foi possivel atualizar insumo, erro interno")

@router.delete("/deleta/{id}")
async def delete_insumos(id: int, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/delete/{id}</code>
        Deleta dados através de um ID"""
    
    insumos_controller.get_id_data(id, db)
    
    try:
        insumos_controller.delete_by_id(id, db)
        msg = "Dados excluídos com sucesso"
        return {"mensagem": msg, "status": 204}
    except Exception as e:
        HTTPException(500, detail="Nao foi possivel deletar insumo, erro interno")