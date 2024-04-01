from fastapi import APIRouter
import requests


currency_router = APIRouter(prefix='/currency', tags=['Курсы валют'])


# Запросы на получение нужных курсов валют
@currency_router.post('/get_rates')
async def get_currency():
    nbu_url = "https://nbu.uz/exchange-rates/json/"
    usd = requests.get(nbu_url).json()[-1]
    rub = requests.get(nbu_url).json()[-6]
    eur = requests.get(nbu_url).json()[7]
    return {'USD': usd, 'RUB': rub, 'EUR': eur}
