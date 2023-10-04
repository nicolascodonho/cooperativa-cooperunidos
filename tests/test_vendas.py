import sys, os
from fastapi.testclient import TestClient
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from src.main import app
from datetime import datetime

client = TestClient(app)

def get_id(schema: str):
    try:
        data = client.get(f'/{schema}/busca')
        id = data.json()['mensagem'][0]['id']
        return id
    except Exception as e:
        return e
    
def test_create_insumos():
    get_id_fornecedor = get_id('fornecedores')
    insumos = {'id_fornecedor': get_id_fornecedor, 'nome_insumo': 'Cobre'}
    client.post('/insumos/cria', json=insumos)

def test_create_compradores():
    comprador = {'nome_empresa': 'comprador-teste'}
    client.post('/compradores/cria', json=comprador)
    
def test_create_vendas():
    id_insumo = get_id('insumos')
    id_comprador = get_id('compradores')
    peso = 14
    responsavel = 'responsavel-teste'
    valor = 20.00
    data_venda = datetime.utcnow()
    data_formatada = data_venda.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    ## Possibilidades de tomar um not json serializable: o id_insumo e o id_comprador podem não existir
    vendas = {
        'id_insumo': id_insumo, 
        'id_comprador': id_comprador, 
        'peso': peso, 
        'responsavel': responsavel, 
        'data_venda': data_formatada,
        'valor': valor
    }
    
    res = client.post('/vendas/cria', json=vendas)
    assert res.json()['status'] == 201
    assert res.json()['mensagem'] == "Dados criados com sucesso"

def test_get_vendas():
    res = client.get('/vendas/busca')
    assert res.json()['mensagem'][0]['responsavel'] == 'responsavel-teste'
    assert res.json()['status'] == 200

def test_get_vendas_by_id():
    id = get_id('vendas')
    res = client.get(f'/vendas/busca/{id}')
    assert res.json()['mensagem']['data_venda'] == '2023-10-04'

# def test_update_vendas():
#     id = get_id('vendas')
#     id_fornecedor = get_id('fornecedores')
#     insumo = {'nome_insumo': 'Ferro', 'id_fornecedor': id_fornecedor}
#     res = client.put(f'/vendas/atualiza/{id}', json=insumo)

#     assert res.json()['status'] == 204
#     assert res.json()['mensagem'] == 'Dados atualizados com sucesso'

def test_delete_vendas():
    id = get_id('vendas')
    res = client.delete(f'/vendas/deleta/{id}')

    assert res.json()['status'] == 204
    assert res.json()['mensagem'] == 'Dados excluídos com sucesso'