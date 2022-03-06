from app import create_app

from config import DevConfig

from app.models.profile import Profile
from app.models.portfolio import Portfolio
from app.models.coin import Coin

app = create_app(DevConfig)
