import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.routes import insumos
from src.routes import vendas
from src.routes import compradores
from src.routes import fornecedores
from src.routes import usuarios

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def handle_invalid_request(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        if "Invalid token" in str(e) or "Expired token" in str(e) or "Signature has expired" in str(e):
            return JSONResponse(status_code=403, content={"detail": "Token expirado ou invalidado, por favor, faça o logout e login novamente"})

app.include_router(vendas.router, prefix="/vendas")
app.include_router(insumos.router, prefix="/insumos")
app.include_router(compradores.router, prefix="/compradores")
app.include_router(fornecedores.router, prefix="/fornecedores")
app.include_router(usuarios.router)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


@app.get("/")
def root():
    return {
        "message": "Olá, essa é a pagina inicial da api. Para visualizar as rotas existentes na mesma, utilize a rota /docs ou /redoc.",
    }
