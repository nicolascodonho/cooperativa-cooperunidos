from sqlalchemy import Column, String, Integer, Date
from connection import Base

class Insumos(Base):
    __tablename__ = "insumos"
    id = Column('id', Integer, primary_key=True, index=True)
    material = Column('material', String(100))
    quantidade = Column('quantidade', Integer)
    data = Column('data', Date)
    nome = Column('nome', String(100))