import sys, os, json
from fastapi.testclient import TestClient
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from src.main import app

client = TestClient(app)

def test_create_fornecedores():
    fornecedor = {'nome': 'fornecedor-teste', 'empresa': True}
    res = client.post('/fornecedores/cria', json=fornecedor)
    # assert res.status_code == 201
    assert res.json()['mensagem'] == "Dados criados com sucesso"

def test_get_fornecedores():
    res = client.get('/fornecedores/busca')
    assert res.status_code == 200
    assert res.json() == 'cleber'

