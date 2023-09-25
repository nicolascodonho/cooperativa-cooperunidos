# Projeto Integrador - Cooperativa Cooperunidos

O presente projeto visa atender uma demanda de cadastros de insumos recebidos pela cooperativa. Em resumo, um CRUD.

## Ferramentas:

- Python
- Angular
- MySQL
- Docker

## Fases do projeto:

Infraestrutura:
- [x] Criar dockerfile do projeto
- [x] Estabelecer a comunicação entre os componentes para funcionamento do projeto

Backend (API):
- [x] Criar as funções responsáveis por cada rota
- [x] Criar modelos para requisição
- [x] Criar rotas
- [x] Criar integração com banco de dados

## Segunda etapa do projeto:
Cobertura de testes.

Alguns adendos para que os testes possam rodar:
- Todos os testes estão dentro do diretório *tests*
- Para roda-los, é necessário que o banco de dados esteja rodando e devidamente configurado. Caso vá testar localmente, utilize o comando:
```docker compose up db``` ou 
```docker-compose up db``` 
vai depender de qual ferramenta você tem disponível, para tal visite a [documentação](https://docs.docker.com/compose/gettingstarted/) e veja as configurações.
- Por ultimo, utilize o comando:
```pytest```