from datetime import datetime
from pydantic import BaseModel

class Insumos(BaseModel):
    id: int
    material: str
    quantidade: int
    data: datetime
    nome: str

    class Config:
        orm_mode = True