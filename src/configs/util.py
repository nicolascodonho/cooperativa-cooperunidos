import requests
from fastapi.exceptions import HTTPException
from fastapi import status, Depends
from fastapi.security import OAuth2PasswordBearer
from dotenv import dotenv_values
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

config = dotenv_values(".env")

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)

def get_current_user(token: str = Depends(reuseable_oauth)):
    payload = jwt.decode(token, config['JWT_SECRET_KEY'], config['ALGORITHM'])
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
        expires_delta = datetime.utcnow() + timedelta(minutes=int(config['ACCESS_TOKEN_EXPIRE_MINUTES']))
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, config['JWT_SECRET_KEY'], config['ALGORITHM'])
    return encoded_jwt