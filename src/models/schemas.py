from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Insumos(BaseModel):
    id: int
    material: str
    quantidade: int
    data: Optional[datetime] = datetime.now()
    nome: str

    class Config:
        orm_mode = True