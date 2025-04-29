import sqlalchemy
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import Session,sessionmaker


DB_URL = "sqlite:///./test.db"
engine = create_engine(DB_URL)
SessionLocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = sqlalchemy.orm.declarative_base()

