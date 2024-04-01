from fastapi import APIRouter
from card import RegisterCardValidator
from database.transferservice import (create_transaction_db,
                                      get_history_transaction_db,
                                      cancel_transaction_db)

transfer_router = APIRouter(prefix='/transfers', tags=['Работа с транзакциями'])


# Создание перевода
@transfer_router.post('/add')
async def create_transaction(data: RegisterCardValidator):
    result = create_transaction_db(**data.model_dump())
    return {'message': result}


# Получение все переводы по карте, т.е. История
@transfer_router.get('/all')
async def get_history_transaction(card_from_number):
    result = get_history_transaction_db(card_from_number)
    return {'message': result}


# Отмена транзакции
@transfer_router.delete('/cancel')
async def cancel_transaction(card_from, card_to, amount, transfer_id):
    return cancel_transaction_db(card_from, card_to, amount, transfer_id)
