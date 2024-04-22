from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from src.controllers import user_controller
from src.models import schemas, models
from src.database.get_db import get_db
from src.database.connection import engine
from src.configs.util import (
    create_access_token, 
    verify_password, 
    get_current_user,
    reuseable_oauth
)

router = APIRouter(
    tags=["Usuarios"]
)

models.Base.metadata.create_all(bind=engine)

@router.post('/login')
async def login(usuario: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario_db = user_controller.get_user_by_email(db, usuario.username)
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = usuario_db.password
    print(hashed_pass)
    if not verify_password(usuario.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": create_access_token(usuario.username),
    }

# @router.post("/cria")
# async def save_usuarios(usuarios: schemas.UsuariosCreate, db: Session = Depends(get_db)):
#     """
#     <code class='highlight'>/cria</code>
#         Cria usuário baseado nos models """
#     try:
#         user_controller.create_data(db, usuarios)
#         msg = "Dados criados com sucesso"
#         return {"mensagem": msg, "status": 201}
#     except Exception as e:
#         return HTTPException(500, detail="Nao foi possivel criado usuarios, erro interno")

# @router.put("/atualiza/{id}")
# async def update_usuarios(id: int, usuarios: schemas.UsuariosUpdate, db: Session = Depends(get_db)):
#     """
#     <code class='highlight'>/atualiza/{id}</code>
#         Atualiza dados através de um ID"""
    
#     user_controller.get_id_data(id, db)

#     try:
#         user_controller.update_data(id, db, usuarios)
#         msg = "Dados atualizados com sucesso"
#         return {"mensagem": msg, "status": 204}
#     except Exception as e:
#         return HTTPException(500, detail="Nao foi possivel atualizar usuarios, erro interno")

# @router.delete("/deleta/{id}")
# async def delete_usuarios(id: int, user = Depends(get_current_user), db: Session = Depends(get_db)):
#     """
#     <code class='highlight'>/delete/{id}</code>
#         Deleta dados através de um ID"""
      
#     try:
#         user_controller.delete_by_id(id, db)
#         msg = "Dados excluídos com sucesso"
#         return {"mensagem": msg, "status": 204}
#     except Exception as e:
#         HTTPException(500, detail="Nao foi possivel deletar usuarios, erro interno")