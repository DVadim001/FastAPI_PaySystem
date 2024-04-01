from fastapi import APIRouter
from card import RegisterCardValidator
from database.cardservice import (add_card_db,
                                  add_balance_card_db,
                                  get_all_user_card_db,
                                  get_exact_user_card_db,
                                  check_card_db,
                                  change_info_card_db,
                                  delete_card_db)

card_router = APIRouter(prefix='/cards', tags=['Работа с картами'])


# Добавление карты
@card_router.post('/add')
async def add_card(data: RegisterCardValidator):
    result = add_card_db(**data.model_dump())
    return {'message': result}


# Пополнить баланс
@card_router.post('/balance')
async def add_balance_card(card_id, balance):
    return add_balance_card_db(card_id, balance)


# Вывести все карты определнного пользователя
@card_router.get('/all')
async def get_all_user_card(user_id):
    result = get_all_user_card_db(user_id)
    return result


# Вывести определённую карту определённого пользователь
@card_router.get('/user')
async def get_exact_user_card(user_id, card_id):
    result = get_exact_user_card_db(user_id, card_id)
    return {'meaasge': result}


# Проверка карты на наличие в БД
@card_router.get('/check')
async def check_card(card_number):
    result = check_card_db(card_number)
    return {'message': result}


# Изменение данных на карте
@card_router.put('/edit')
async def change_info_card(card_id, card_name_new):
    result = change_info_card_db(card_id, card_name_new)
    return result


# Удаление карты
@card_router.delete('/delete')
async def delete_card(card_id):
    return delete_card_db(card_id)
