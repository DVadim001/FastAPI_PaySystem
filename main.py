from fastapi import FastAPI
from database import Base, engine
from transaction.currency_api import currency_router

app = FastAPI(
    title="Pay System",
    docs_url='/')
Base.metadata.create_all(bind=engine)

app.include_router(currency_router)

# ДЗ - прописать все роутеры и подключить