import datetime

import requests

from app.models.coin import Coin

def _get_most_recent_price_timestamp(coin_id):
    recent_coin = Coin.query.filter_by(coin_id=coin_id).order_by(Coin.timestamp.desc()).first()
    if recent_coin:
        return recent_coin.timestamp
    return datetime.datetime.now() - datetime.timedelta(seconds=600)

def price(coin_id, vs_currency="usd"):
    delta = datetime.datetime.now() - _get_most_recent_price_timestamp(coin_id)
    if delta.seconds < 300:
        return
    base_url = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies={}"
    gecko_url = base_url.format(coin_id, vs_currency)
    gecko_response = requests.get(gecko_url)
    data = gecko_response.json()
    current_value = data[coin_id][vs_currency]

    coin = Coin(coin_id=coin_id, current_value=current_value, timestamp=datetime.datetime.now())
    coin.save()
