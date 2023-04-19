from sqlalchemy import Column, String, Integer, Date
from src.database.connection import Base

class Insumos(Base):
    __tablename__ = "insumos"
    id = Column('id', Integer, primary_key=True, index=True)
    material = Column('material', String(255))
    quantidade = Column('quantidade', Integer)
    data = Column('data_saida', Date)
    nome = Column('nome', String(255))