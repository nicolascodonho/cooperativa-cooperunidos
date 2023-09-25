CREATE DATABASE IF NOT EXISTS cooperunidos;

CREATE TABLE IF NOT EXISTS tb_fornecedores (
    id BIGINT NOT NULL,
    nome VARCHAR(80) NOT NULL,
    empresa BOOLEAN DEFAULT TRUE, /* campo para sabermos se é um empresa ou pessoa física que está fornecendo os insumos*/
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NULL ON UPDATE NOW(),
    CONSTRAINT PK_id_tb_empresas PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS tb_compradores (
    id BIGINT NOT NULL,
    nome_empresa VARCHAR(80) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NULL ON UPDATE NOW(),
    CONSTRAINT PK_id_tb_compradores PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS tb_insumos (
    id BIGINT NOT NULL,
    id_fornecedor BIGINT NOT NULL,
    nome_insumo VARCHAR (80) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NULL ON UPDATE NOW(),
    CONSTRAINT PK_id_tb_insumos PRIMARY KEY (id),
    CONSTRAINT FK_id_tb_fornecedor FOREIGN KEY (id_fornecedor) REFERENCES tb_fornecedores (id) ON DELETE CASCADE
    
);

CREATE TABLE IF NOT EXISTS tb_vendas (
    id BIGINT NOT NULL,
    id_insumo BIGINT NOT NULL,
    id_comprador BIGINT NOT NULL,
    peso DECIMAL NOT NULL,
    data_venda DATE NOT NULL,
    responsavel VARCHAR(30) NOT NULL,
    valor DECIMAL(30, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NULL ON UPDATE NOW(),
    CONSTRAINT PK_id_tb_vendas PRIMARY KEY (id),
    CONSTRAINT FK_id_tb_insumos FOREIGN KEY (id_insumo) REFERENCES tb_insumos (id) ON DELETE CASCADE,
    CONSTRAINT FK_id_tb_compradores FOREIGN KEY (id_comprador) REFERENCES tb_compradores (id) ON DELETE CASCADE
);