from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from src.controllers import insumos_controller
from src.models import schemas, models
from src.database.get_db import get_db
from src.database.connection import engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    tags=["Insumos"]
)

@router.get("/busca")
def get_insumos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/busca</code>
        Retorna os insumos existentes dentro do banco limitados por skip e limit"""
    insumos = insumos_controller.get_all_data(db, skip, limit)
    return insumos, 200

@router.get("/busca/{id}")
def get_insumo(id: int, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/busca/{id}</code>
        Retorna o insumo através de um ID"""
    insumo = insumos_controller.get_id_data(id, db)
    if insumo is None:
        raise HTTPException(status_code=404, detail="Insumo não encontrado")
    return insumo, 200

@router.post("/cria")
async def save(insumos: schemas.Insumos, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/cria</code>
        Cria insumos baseado nos models """
    try:
        await insumos_controller.create_data(db, insumos)
        msg = "Dados criados com sucesso"
        return msg, 200
    except Exception as e:
        print("Não foi possível criar, erro: ", e)

@router.put("/atualiza/{id}")
async def update_data(id: int, insumos: schemas.Insumos, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/atualiza/{id}</code>
        Atualiza dados através de um ID"""
    try:
        await insumos_controller.update_data(id, db, insumos)
        msg = "Dados atualizados com sucesso"
        return msg, 200
    except Exception as e:
        print("Não foi possível criar, erro: ", e)
    

@router.delete("/delete/{id}")
async def delete_by_id(id: int, db: Session = Depends(get_db)):
    """
    <code class='highlight'>/delete/{id}</code>
        Deleta dados através de um ID"""
    try:
        await insumos_controller.delete_by_id(id, db)
        msg = "Dados excluídos com sucesso"
        return msg, 200
    except Exception as e:
        print(e)