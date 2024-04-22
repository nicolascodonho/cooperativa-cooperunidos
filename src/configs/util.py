from fastapi.exceptions import HTTPException
from pydantic import ValidationError
from fastapi import status, Depends
from fastapi.security import OAuth2PasswordBearer
from dotenv import dotenv_values
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

config = dotenv_values(".env")

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = 'ff405abf2fdd424bba28642d345e44dbaa3371cb46f483e72e1c96227cd836a8'
JWT_REFRESH_SECRET_KEY = 'b7899ca2e30698c591229c51739229199ae77c6d40e549028872011249838c26'

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)

def get_current_user(token: str = Depends(reuseable_oauth)):
    payload = jwt.decode(token, JWT_SECRET_KEY, ALGORITHM)
    if datetime.fromtimestamp(payload['exp']) < datetime.now():
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = payload.get('sub')

    if user is None:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Usuario não pode ser validado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

# def get_current_user(db: Session = Depends(get_db), token: str = Depends(reuseable_oauth)):
#     try:
#         payload = jwt.decode(
#             token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
#         )        
        
#         if datetime.fromtimestamp(payload['exp']) < datetime.now():
#             raise HTTPException(
#                 status_code = status.HTTP_401_UNAUTHORIZED,
#                 detail="Token expired",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
#     except(jwt.JWTError, ValidationError):
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
    
#     user = get_user_by_email(db, payload['email'])

#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Could not find user",
#         )
    
#     return user