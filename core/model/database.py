from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = config("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
DBSession = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
