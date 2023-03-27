from sqlalchemy.orm import Session
import schemas, models

def create_data(db: Session, insumos: schemas.Insumos):
    data = models.Insumos(**insumos.dict())

    db.add(data)
    db.commit()
    db.refresh(data)

    return data

def get_all_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Insumos).offset(skip).limit(limit).all()
