from fastapi import FastAPI
import logging
from routes import insumos_routes

app = FastAPI()
app.include_router(insumos_routes.router)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

@app.get("/")
def root():
    return {
        "message": "Olá, essa é a pagina inicial da api. Para visualizar as rotas existentes na mesma, utilize a rota /docs.",
    }
