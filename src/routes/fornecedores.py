from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from src.models import schemas, models
from src.database.get_db import get_db
from src.database.connection import engine
from src.controllers import fornecedor_controller 

router = APIRouter(
    tags=["Fornecedores"]
)

models.Base.metadata.create_all(bind=engine)


@router.get("/busca")
def get_fornecedores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):

    fornecedor = fornecedor_controller.get_all_data(db, skip, limit)
    if not fornecedor:
        return HTTPException(404, detail="Lista de fornecedor vazia!")
    return fornecedor, 200

@router.get("/busca/{id}")
def get_fornecedor(id: int, db: Session = Depends(get_db)):
    fornecedor = fornecedor_controller.get_id_data(id, db)
    return fornecedor, 200

@router.post("/cria")
async def save_fornecedor(fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    try:
        fornecedor_controller.create_data(db, fornecedor)
        return "Dados criados com sucesso", 201
    except Exception as e:
        print(e)
        raise HTTPException(500, detail="Nao foi possível criar dados, erro interno")
        
@router.put("/atualiza/{id}")
async def update_fornecedor(id: int, fornecedor: schemas.FornecedorUpdate, db: Session = Depends(get_db)):
    
    fornecedor_controller.get_id_data(id, db)
    
    try:
        fornecedor_controller.update_data(id, db, fornecedor)
        return "Dados atualizados com sucesso", 204
    except Exception as e:
        return HTTPException(500, detail="Nao foi possivel atualizar dados, erro interno")
    
@router.delete("/deleta/{id}")
async def delete_fornecedor(id: int, db: Session = Depends(get_db)):

    fornecedor_controller.get_id_data(id, db)

    try:
        fornecedor_controller.delete_by_id(id, db)
        msg = "Dados excluídos com sucesso"
        return msg, 200
    except Exception as e:
        print(e)
        return HTTPException(500, detail="Nao foi possivel deletar dados, erro interno")