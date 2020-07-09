from flask import session, redirect, request, url_for
from orator.exceptions.orm import ModelNotFound
from flask_login import login_user

from functools import wraps
import jwt

from auth_encryption.encryption import Encryption
from recipe.models.user import User

def auth(func):

    @wraps(func)
    def wrapped(*args, **kwargs):
        from recipe import app
        
        # Get Authorization header
        bearer = request.headers.get('Authorization')

        # If header doesn't exists 
        if not bearer:
            return {'message': 'Authentication token is missing'}, 403
        
        # If token valid, continue else throw exception
        try:
            # Get the token, from the Authorization header
            token = bearer.split(" ")[1]
            j = jwt.decode(token, app.config['SECRET_KEY'])

            # Decrypt the token
            encryption = Encryption()
            u = encryption.decrypt(j.get('username'))

            # Check if 
            try:
                user = User.where_username(u).first_or_fail()
            except ModelNotFound:
                return {'message':'You are not authorized'}, 403
        except:
            return {'message': 'Invalid token provided'}, 403
        
        return func(*args, **kwargs)
    return wrapped