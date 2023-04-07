from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter
from src.controllers import insumos_controller
from src.models import schemas
from src.database import get_db

router = APIRouter(
    tags=["Insumos"]
)

@router.get("/busca", response_model = list[schemas.Insumos])
def get_insumos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    insumos = insumos_controller.get_all_data(db, skip, limit)
    
    return insumos, 200

@router.get("/busca/{id}", response_model=schemas.Insumos)
def get_insumo(id: int, db: Session = Depends(get_db)):
    insumo = insumos_controller.get_id_data(db, id=id)
    if insumo is None:
        raise HTTPException(status_code=404, detail="Insumo não encontrado")
    return insumo, 200

@router.post("/cria", response_model=schemas.Insumos)
async def save(insumos: schemas.Insumos, db: Session = Depends(get_db)):
    try:
        data = await insumos_controller.create_data(db, insumos)
        return data, 200
    except Exception as e:
        print(e)

@router.put("/atualiza/{id}", response_model=schemas.Insumos)
def update_data(id: int, insumos: schemas.Insumos, db: Session = Depends(get_db)):
    try:
        data = insumos_controller.update_data(id, db, insumos)
        return data, 200
    except Exception as e:
        print(e)
    

@router.delete("/delete/{id}", response_model=schemas.Insumos)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    try:
        data = insumos_controller.delete_by_id(id, db)
        return data, 200
    except Exception as e:
        print(e)