from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class InsumosBase(BaseModel):
    id_fornecedor: int
    nome_insumo: str

class InsumosCreate(InsumosBase):
    pass

class InsumosUpdate(InsumosBase):
    pass

class Insumos(InsumosBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class VendasBase(BaseModel):
    id_insumo: int
    id_comprador: int
    peso: float
    responsavel: str
    valor: float
    data_venda: Optional[datetime]

class VendasCreate(VendasBase):
    pass

class VendasUpdate(VendasBase):
    pass

class Vendas(VendasBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class FornecedorBase(BaseModel):
    nome: str
    empresa: bool

class FornecedorCreate(FornecedorBase):
    pass

class FornecedorUpdate(FornecedorBase):
    pass

class Fornecedor(FornecedorBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class CompradoresBase(BaseModel):
    nome_empresa: str

class CompradoresCreate(CompradoresBase):
    pass

class CompradoresUpdate(CompradoresBase):
    pass

class Compradores(CompradoresBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class UsuariosBase(BaseModel):
    email: str
    password: str

class UsuariosCreate(UsuariosBase):
    pass
    
class UsuariosUpdate(UsuariosBase):
    pass

class Usuarios(UsuariosBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True