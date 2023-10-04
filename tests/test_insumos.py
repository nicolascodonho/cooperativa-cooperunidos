import sys, os
from fastapi.testclient import TestClient
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from src.main import app

client = TestClient(app)


def get_id(schema: str):
    data = client.get(f'/{schema}/busca')
    id = data.json()['mensagem'][0]['id']
    return id

def test_create_insumos():
    get_id_fornecedor = get_id('fornecedores')
    insumos = {'id_fornecedor': get_id_fornecedor, 'nome_insumo': 'Cobre'}
    res = client.post('/insumos/cria', json=insumos)
    assert res.json()['status'] == 201
    assert res.json()['mensagem'] == "Dados criados com sucesso"

def test_get_insumos():
    res = client.get('/insumos/busca')
    assert res.json()['mensagem'][0]['nome_insumo'] == 'Cobre'

def test_get_insumos_by_id():
    id = get_id('insumos')
    res = client.get(f'/insumos/busca/{id}')
    assert res.json()['mensagem']['nome_insumo'] == 'Cobre'

def test_update_insumos():
    id = get_id('insumos')
    id_fornecedor = get_id('fornecedores')
    insumo = {'nome_insumo': 'Ferro', 'id_fornecedor': id_fornecedor}
    res = client.put(f'/insumos/atualiza/{id}', json=insumo)

    assert res.json()['status'] == 204
    assert res.json()['mensagem'] == 'Dados atualizados com sucesso'

def test_delete_insumos():
    id = get_id('insumos')
    res = client.delete(f'/insumos/deleta/{id}')

    assert res.json()['status'] == 204
    assert res.json()['mensagem'] == 'Dados excluídos com sucesso'