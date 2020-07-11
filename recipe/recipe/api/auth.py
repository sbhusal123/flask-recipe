from flask import Blueprint
from flask_restful import Api, Resource, request
from flask_login import current_user

from recipe.api.validators.auth_validator import LoginValidator, RegisterValidator
from auth_encryption.encryption import Encryption
from recipe.models.user import User
from recipe import app as application

from orator.exceptions.query import QueryException
from orator.exceptions.orm import ModelNotFound

from werkzeug.security import check_password_hash
import datetime
import jwt


class AuthLogin(Resource):

    def post(self):
        data = LoginValidator().validate()
        user = User.where_username(data.username).first()

        if not user:
            return {'message': 'Credentials did not match.', 'code': 401}, 401

        if check_password_hash(user.password, data.password) == False:
            return {'message': 'Credentials did not match.', 'code': 401}, 401

        try:
            encryption = Encryption()

            # Generate JWT Bearer Token using username
            token = jwt.encode({'hash': encryption.encrypt(str(user.username)), 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, application.config['SECRET_KEY'])
            return {'token': token.decode('utf-8'), 'code': 200}, 200
        except Exception as e:
            print(e)
            return {'message': 'Unable to login, try again later.', 'code': 401}, 401

class AuthRegister(Resource):
    
    def post(self):
        data = RegisterValidator().validate()

        if data.password != data.confirm_password:
            return {'message': 'Password did not match.'}, 400

        user = User.where('username', data.username).first()

        if user:
            return {'message': 'User already registered with this details', 'code': 400}, 400

        user = User.create(data)

        return {'message': 'User registered successfully.', 'data': user.serialize(), 'code': 201}, 201



auth_api = Blueprint('recipe.api.auth', __name__)
api = Api(auth_api)

api.add_resource(AuthLogin, '/login', endpoint='login')
api.add_resource(AuthRegister, '/register', endpoint='register')
