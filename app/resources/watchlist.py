from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user

from app.models.profile import Profile
from app.models.watchlist import Watchlist
from app.models.coin import Coin
from app.gecko.simple import price

from app import db 

class WatchlistResource(Resource):
    @jwt_required()
    def get(self):
        watchlist = Watchlist.query.filter_by(profile=current_user).all()
        watchlist_dict = {}
        for investment in watchlist:
            price(investment.coin_id)
            coin = Coin.query.filter_by(coin_id=investment.coin_id).order_by(Coin.timestamp.desc()).first()
            watchlist_dict[coin.coin_id] = coin.current_value

        return {
            "watchlist": watchlist_dict,
            "username": current_user.username
        }, HTTPStatus.OK
        

class ManageWatchlistResource(Resource):
    @jwt_required()
    def post(self, coin_id):
        watchlist = Watchlist(coin_id=coin_id, profile=current_user)
        watchlist.save()

        return {"message": f"Added {coin_id} to {current_user.username} watchlist"}, HTTPStatus.CREATED

    @jwt_required()
    def delete(self, coin_id):
        watchlist = Watchlist.query.filter_by(profile=current_user).filter_by(coin_id=coin_id).delete()
        db.session.commit()

        return {"message": f"Removed {coin_id} from {current_user.username} watchlist"}, HTTPStatus.NO_CONTENT