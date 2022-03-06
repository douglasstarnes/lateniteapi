from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.profile import Profile
from app.models.portfolio import Portfolio
from app.models.coin import Coin

from app import db 

class PortfolioResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        profile = Profile.query.filter_by(username=current_user).first()
        portfolio = Portfolio.query.filter_by(profile=profile).all()
        portfolio_dict = {}
        for investment in portfolio:
            coin = Coin.query.filter_by(coin_id=investment.coin_id).order_by(Coin.timestamp.desc()).first()
            portfolio_dict[coin.coin_id] = coin.current_value

        return portfolio_dict, HTTPStatus.OK
        

class ManagePortfolioResource(Resource):
    @jwt_required()
    def post(self, coin_id):
        current_user = get_jwt_identity()
        profile = Profile.query.filter_by(username=current_user).first()

        portfolio = Portfolio(coin_id=coin_id, profile=profile)
        portfolio.save()

        return {"message": f"Added {coin_id} to portfolio"}, HTTPStatus.CREATED

    @jwt_required()
    def delete(self, coin_id):
        current_user = get_jwt_identity()
        profile = Profile.query.filter_by(username=current_user).first()
        portfolio = Portfolio.query.filter_by(profile=profile).filter_by(coin_id=coin_id).delete()
        db.session.commit()

        return {"message": f"Removed {coin_id} from portfolio"}, HTTPStatus.NO_CONTENT