from pydantic import BaseModel


class RegisterUserValidator(BaseModel):
    name: str
    lastname: str
    phone_number: int
    email: str
    country: str
    password: str


class EditUserValidator(BaseModel):
    user_id: int
    edit_info: str
    new_info: str
