from fastapi import FastAPI

dns = "127.0.0.1"
port = "8000"

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Olá, essa é a pagina inicial da api. Para visualizar as rotas existentes na mesma, utilize a rota /docs.",
        "link": f"{dns}:{port}/docs"
    }