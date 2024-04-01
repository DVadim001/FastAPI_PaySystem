from pydantic import BaseModel


class RegisterCardValidator(BaseModel):
    user_id: int
    card_name: str
    card_number: int
    cvv: int
    exp_date: str
