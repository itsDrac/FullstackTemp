from sqlmodel import SQLModel, create_engine, Field, Session
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = os.environ.get("DB_PASSWORD")
POSTGRES_DB = "postgres"
POSTGRES_HOST = "database"
POSTGRES_PORT = "5432"

print(os.environ.get("DB_PASSWORD"))

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


engine = create_engine(DATABASE_URL)

def create_metadata():
    SQLModel.metadata.create_all(engine)

def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
