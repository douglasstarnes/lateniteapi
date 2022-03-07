from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    jwt.init_app(app)

    Migrate(app, db)
    api = Api(app)

    from app.resources.auth import LoginResource, RegisterResource
    from app.resources.watchlist import WatchlistResource, ManageWatchlistResource

    api.add_resource(LoginResource, "/auth/login")
    api.add_resource(RegisterResource, "/auth/register")
    api.add_resource(WatchlistResource, "/watchlist")
    api.add_resource(ManageWatchlistResource, "/watchlist/<coin_id>")

    return app
