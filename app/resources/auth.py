from http import HTTPStatus
from flask_restful import Resource
from flask import request
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

from app.models.profile import Profile

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        profile = Profile.query.filter_by(username=username).first()

        if not profile:
            return {"error": "Try again"}, HTTPStatus.BAD_REQUEST 

        if not check_password_hash(profile.password_hash, password):
            return {"error": "Invalid credentials"}, HTTPStatus.UNAUTHORIZED

        access_token = create_access_token(identity=username)

        return {"access_token": access_token}, HTTPStatus.OK
        
class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        profile = Profile.query.filter_by(username=username).first()

        if profile:
            return {"error": f"Username {username} already exists"}

        profile = Profile(username=username, password=password)
        profile.save()

        return {
            "id": profile.id,
            "username": profile.username
        }, HTTPStatus.CREATED
