from pydantic import BaseModel


class TransactionValidate(BaseModel):
    card_from: int
    card_to: int
    amount: float
