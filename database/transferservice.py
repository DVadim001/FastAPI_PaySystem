from database.models import UserCard, Tranfer
from datetime import datetime
from database import get_db


# Проверка карты
def validate_card(card_number, db):
    exact_card = db.query(UserCard).filter_by(card_number=card_number)
    return exact_card


# Создание перевода
def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    # Проверка на наличие обеих карт в БД
    checker_card_from = validate_card(card_from, db)
    checker_card_to = validate_card(card_to, db)

    # Если обе карты существуют в БД, то делаем транзакцию
    if checker_card_from and checker_card_to:
        # Проверка баланса отправителя
        if checker_card_from.balance >= amount:
            # Минусуем у тего, кто отправляет деньги
            card_from.balance -= amount
            # Добавим тому, кто получает
            card_to.balance += amount

            # Сохраняем платёж в БД
            new_transaction = Tranfer(card_from_number=checker_card_from.card_number,
                                      card_to_number=checker_card_to.card_number,
                                      amount=amount,
                                      transaction_date=datetime.now())
            db.add(new_transaction)
            db.commit()
            return "Перевод успешно выполнен"
        else:
            return "Недостаточно средств"
    else:
        return "Одна из карт не существует"


# Получение все переводы по карте, т.е. История
def get_history_transaction(card_from_number):
    db = next(get_db())

    card_transaction = db.query(Tranfer).filter_by(card_from_number=card_from_number).all()
    if card_transaction:
        return card_transaction
    else:
        return "Истории нет"


# Отмена транзакции. Подсказка status = False
def cancel_transaction_db(card_from, card_to, amount):
    pass
