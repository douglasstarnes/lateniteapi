import datetime

import requests

from app.models.coin import Coin

def price(coin_id, vs_currency):
    base_url = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies={}"
    gecko_url = base_url.format(coin_id, vs_currency)
    gecko_response = requests.get(gecko_url)
    data = gecko_response.json()
    current_value = data[coin_id][vs_currency]

    coin = Coin(coin_id=coin_id, current_value=current_value, timestamp=datetime.datetime.now())
    coin.save()
