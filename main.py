from app import create_app

from config import ProdConfig

from app.models.profile import Profile
from app.models.watchlist import Watchlist
from app.models.coin import Coin

app = create_app(ProdConfig)
