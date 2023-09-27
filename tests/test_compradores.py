import sys, os
from fastapi.testclient import TestClient
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from src.main import app

client = TestClient(app)

def get_id():
    data = client.get('/compradores/busca')
    id = data.json()['mensagem'][0]['id']
    return id

def test_create_compradores():
    comprador = {'nome_empresa': 'comprador-teste'}
    res = client.post('/compradores/cria', json=comprador)
    assert res.json()['status'] == 201
    assert res.json()['mensagem'] == "Dados criados com sucesso"

def test_get_compradores():
    res = client.get('/compradores/busca')
    assert res.json()['mensagem'][0]['nome_empresa'] == 'comprador-teste'

def test_get_compradores_by_id():
    id = get_id()
    res = client.get(f'/compradores/busca/{id}')
    assert res.json()['mensagem']['nome_empresa'] == 'comprador-teste'

def test_update_compradores():
    id = get_id()
    comprador = {'nome_empresa': 'novo-comprador'}
    res = client.put(f'/compradores/atualiza/{id}', json=comprador)

    assert res.json()['status'] == 204
    assert res.json()['mensagem'] == 'Dados atualizados com sucesso'

def test_delete_compradores():
    id = get_id()
    res = client.delete(f'/compradores/deleta/{id}')

    assert res.json()['status'] == 204
    assert res.json()['mensagem'] == 'Dados excluídos com sucesso'