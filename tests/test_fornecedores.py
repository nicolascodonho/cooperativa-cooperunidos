import sys, os
from fastapi.testclient import TestClient
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from src.main import app

client = TestClient(app)

def get_id():
    data = client.get('/fornecedores/busca')
    id = data.json()['mensagem'][0]['id']
    return id

def test_create_fornecedores():
    fornecedor = {'nome': 'fornecedor-teste', 'empresa': True}
    res = client.post('/fornecedores/cria', json=fornecedor)
    assert res.json()['status'] == 201
    assert res.json()['mensagem'] == "Dados criados com sucesso"

def test_get_fornecedores():
    res = client.get('/fornecedores/busca')
    assert res.json()['mensagem'][0]['nome'] == 'fornecedor-teste'

def test_get_fornecedores_by_id():
    id = get_id()
    res = client.get(f'/fornecedores/busca/{id}')
    assert res.json()['mensagem']['nome'] == 'fornecedor-teste'

def test_update_fornecedores():
    id = get_id()
    fornecedor = {'nome': 'novo-fornecedor', 'empresa': True}
    res = client.put(f'/fornecedores/atualiza/{id}', json=fornecedor)

    assert res.json()['status'] == 204
    assert res.json()['mensagem'] == 'Dados atualizados com sucesso'

def test_delete_fornecedores():
    id = get_id()
    res = client.delete(f'/fornecedores/deleta/{id}')

    assert res.json()['status'] == 204
    assert res.json()['mensagem'] == 'Dados excluídos com sucesso'