from fastapi import FastAPI
from database import Base, engine
from transfer.currency_api import currency_router
from users.user_api import user_router
from card.card_api import card_router
from transfer.transfer_api import transfer_router

app = FastAPI(
    title="Pay System",
    docs_url='/')
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(currency_router)
app.include_router(card_router)
app.include_router(transfer_router)
