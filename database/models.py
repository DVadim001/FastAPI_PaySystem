from sqlalchemy import Column, String, Integer, DateTime, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base


class Transaction(Base):
    __tablename__ = 'transactions'
    tran_id = Column(Integer, primary_key=True, autoincrement=True)
    tran_date = Column(DateTime)  # Когда перевели
    amount = Column(Float)  # Какая сумма была

    sender_id = Column(Integer, ForeignKey('users.user_id'))
    cart_id = Column(Integer, ForeignKey('carts.cart_id'))
    recipient_id = Column(Integer, ForeignKey('users.user_id'))  # Если получатель тоже пользователь системы

    # Связи для доступа к отправителю, карте и получателю
    sender = relationship('User', foreign_keys=[sender_id], back_populates='transaction_sent')
    cart = relationship('Cart', foreign_keys=[cart_id], back_populates='transactions')
    recipient = relationship('User', foreign_keys=[recipient_id], back_populates='transaction_received')


# Таблица пользователя
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    lastname = Column(String)
    phone_number = Column(String, unique=True)
    email = Column(String)
    password = Column(String)
    country = Column(String)
    profile_photo = Column(String)
    reg_date = Column(DateTime)

    carts = relationship('Cart', back_populates='cart_holder')
    transaction_sent = relationship('Transaction', foreign_keys=[Transaction.sender_id])
    transaction_received = relationship('Transaction', foreign_keys=[Transaction.recipient_id])


class Cart(Base):
    __tablename__ = 'carts'
    cart_id = Column(Integer, primary_key=True, autoincrement=True)
    cart_name = Column(String)
    expiry_date = Column(Date)
    balance = Column(Float)
    type = Column(String)  # (Виза, Мастеркарт, обычная и т.д.)
    cvv = Column(Integer)
    cart_number = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.user_id'))

    transactions = relationship('Transaction', foreign_keys=[Transaction. cart_id])
    cart_holder = relationship('User', back_populates='carts')
