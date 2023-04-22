from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from src.routes import insumos
from src.routes import vendas
from src.routes import compradores
from src.routes import fornecedores

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vendas.router, prefix="/vendas")
app.include_router(insumos.router, prefix="/insumos")
app.include_router(compradores.router, prefix="/compradores")
app.include_router(fornecedores.router, prefix="/fornecedores")

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

@app.get("/")
def root():
    return {
        "message": "Olá, essa é a pagina inicial da api. Para visualizar as rotas existentes na mesma, utilize a rota /docs ou /redoc.",
    }
