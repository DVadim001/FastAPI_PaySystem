from fastapi import FastAPI
from database import Base, engine

app = FastAPI(
    title="Pay System",
    docs_url='/')
Base.metadata.create_all(bind=engine)

