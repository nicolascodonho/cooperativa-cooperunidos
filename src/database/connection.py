from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.configs.util import config

user = config["MYSQL_USER"]
pwd = config["MYSQL_ROOT_PASSWORD"]
host = config["MYSQL_HOST"]
db = config["MYSQL_DATABASE"]
port = config["MYSQL_PORT"]


SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()