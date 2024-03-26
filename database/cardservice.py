from database.models import UserCard
from datetime import datetime
from database import get_db


# Добавление карты
def add_card_db(user_id, card_name, card_number, cvv, exp_date):
    db = next(get_db())
    new_card = UserCard(user_id=user_id, card_name=card_name, card_number=card_number, cvv=cvv, exp_date=exp_date)
    if new_card:
        db.add(new_card)
        db.commit()
        return "Карта успешно добавлена"
    else:
        return "Ошибка добавления"


# Пополнить баланс
def add_balance_card_db(card_id, balance):
    db = next(get_db())
    new_balance = db.query(UserCard).filter_by(card_id=card_id).first()
    if new_balance:
        new_balance.balance += balance
    else:
        return "Данной картыне существует"


# Вывести все карты определнного пользователя
def get_all_user_card_db(user_id):
    db = next(get_db())
    exact_user_card = db.query(UserCard).filter_by(user_id=user_id).first()
    if exact_user_card:
        return exact_user_card
    else:
        return "Данного пользователя нет"


# Вывести определённую карту определённого пользователь
def get_exact_user_card_db(user_id, card_id):
    db = next(get_db())
    exact = db.query(UserCard).filter_by(user_id=user_id, card_id=card_id).first()
    if exact:
        return exact
    else:
        return "Данной карты нет"


# Проверка карты на наличие в БД
def check_card_db(card_number):
    db = next(get_db())
    checker = db.query(UserCard).filter_by(card_number=card_number).first()
    if checker:
        return checker
    else:
        return "Данной карты нет"


# Удаление карты
def delete_card_db(card_id):
    db = next(get_db())
    delete_card = db.query(UserCard).filter_by(card_id=card_id).first()
    if delete_card:
        db.delete(delete_card)
        db.commit()
        return "Карта успешно удалена"
    else:
        return "Карта не найдена"


# Изменение данных на карте
def change_info_card_db(card_id, card_name_new):
    db = next(get_db())
    card_info = db.query(UserCard).filter_by(card_id=card_id).first()
    if card_info:
        card_info.card_name = card_name_new
        db.commit()
        return "Данные изменены"
    else:
        return "Карта не найдена"

