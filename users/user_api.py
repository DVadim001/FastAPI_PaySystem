from fastapi import APIRouter
from users import RegisterUserValidator, EditUserValidator
from database.userservice import (register_user_db,
                                  get_exact_user_db,
                                  get_all_users_db,
                                  check_user_email_db,
                                  edit_user_db,
                                  delete_user_db)

user_router = APIRouter(prefix='/users', tags=['Управление пользователями'])


# Регистрация
@user_router.post('/register')
async def register_user(data: RegisterUserValidator):
    result = register_user_db(**data.model_dump())
    return {'message': result}


# Получить всех пользователей
@user_router.get('/all')
async def get_all_users():
    return get_all_users_db()


# Получить определённого пользователя
@user_router.get('/one')
async def get_exact_user(user_id: int):
    exact_user = get_exact_user_db(user_id)
    return exact_user


# Валидация - проверка через email
@user_router.post('/validation')
async def check_user_email(email):
    valid_email = check_user_email_db(email)
    return valid_email


# Изменить данные у определённого пользователя
@user_router.put('/edit')
async def edit_user(data: EditUserValidator):
    change_data = data.model_dump()
    result = edit_user_db(**change_data)
    return result


# Удаление пользователя
@user_router.delete('/delete')
async def delete_user(user_id: int):
    user = delete_user_db(user_id)
    return user
