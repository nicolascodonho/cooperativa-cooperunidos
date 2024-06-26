from sqlalchemy import (
    Column, 
    String, 
    BigInteger, 
    ForeignKey, 
    DateTime, 
    DECIMAL,
    BOOLEAN
)
from sqlalchemy.orm import relationship
from src.database.connection import Base
from datetime import datetime

class Insumos(Base):
    __tablename__ = "tb_insumos"
    id = Column('id', BigInteger, primary_key=True, index=True)
    id_fornecedor = Column(BigInteger, ForeignKey('tb_fornecedores.id', ondelete='CASCADE'))
    nome_insumo = Column('nome_insumo', String(80), nullable=False)
    created_at = Column('created_at', DateTime, default=datetime.utcnow)
    updated_at = Column('updated_at', DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    fornecedor = relationship("Fornecedor", back_populates="insumos", passive_deletes=True)

class Fornecedor(Base):
    __tablename__ = "tb_fornecedores"
    id = Column('id', BigInteger, primary_key=True, index=True)
    nome = Column('nome', String(80), nullable=False)
    empresa = Column('empresa', BOOLEAN(True), nullable=False)
    created_at = Column('created_at', DateTime, default=datetime.utcnow)
    updated_at = Column('updated_at', DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    insumos = relationship("Insumos", back_populates="fornecedor", passive_deletes=True)

class Compradores(Base):
    __tablename__ = "tb_compradores"
    id = Column('id', BigInteger, primary_key=True, index=True)
    nome_empresa = Column('nome_empresa', String(80), nullable=False)
    created_at = Column('created_at', DateTime, default=datetime.utcnow)
    updated_at = Column('updated_at', DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Vendas(Base):
    __tablename__ = 'tb_vendas'
    id = Column('id', BigInteger, primary_key=True, index=True)
    id_insumo = Column(BigInteger, ForeignKey('tb_insumos.id', passive_deletes=True))
    id_comprador = Column(BigInteger, ForeignKey('tb_compradores.id', passive_deletes=True))
    peso = Column('peso', DECIMAL, nullable=False)
    data_venda = Column('data_venda', DateTime)
    responsavel = Column('responsavel', String(30), nullable=False)
    valor= Column('valor', DECIMAL(30, 2), nullable=False)
    created_at = Column('created_at', DateTime, default=datetime.utcnow)
    updated_at = Column('updated_at', DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Usuarios(Base):
    __tablename__ = 'tb_users'
    id = Column('id', BigInteger, primary_key=True, index=True)
    email = Column('email', String(80), nullable=False)
    password = Column('password', String(80), nullable=False)
    created_at = Column('created_at', DateTime, default=datetime.utcnow)
    updated_at = Column('updated_at', DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)