from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user

from app.models.profile import Profile
from app.models.portfolio import Portfolio
from app.models.coin import Coin

from app import db 

class PortfolioResource(Resource):
    @jwt_required()
    def get(self):
        portfolio = Portfolio.query.filter_by(profile=current_user).all()
        portfolio_dict = {}
        for investment in portfolio:
            coin = Coin.query.filter_by(coin_id=investment.coin_id).order_by(Coin.timestamp.desc()).first()
            portfolio_dict[coin.coin_id] = coin.current_value

        return portfolio_dict, HTTPStatus.OK
        

class ManagePortfolioResource(Resource):
    @jwt_required()
    def post(self, coin_id):
        portfolio = Portfolio(coin_id=coin_id, profile=current_user)
        portfolio.save()

        return {"message": f"Added {coin_id} to portfolio"}, HTTPStatus.CREATED

    @jwt_required()
    def delete(self, coin_id):
        portfolio = Portfolio.query.filter_by(profile=current_user).filter_by(coin_id=coin_id).delete()
        db.session.commit()

        return {"message": f"Removed {coin_id} from portfolio"}, HTTPStatus.NO_CONTENT