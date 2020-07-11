import unittest
from . import version

from recipe import app
from . import version
from recipe.models.user import User
from recipe.models.recipe import Recipe


from factories.user_factory import factory
from factories.recipe_factory import factory as recipe_factory

import jwt
import datetime
from recipe import app
from auth_encryption.encryption import Encryption 


class TestRegisterUser(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    # test creating new user succesfull
    def test_create_new_user(self):
        user_data = factory(User).make(username="adasdas")._attributes
        user_data['confirm_password'] = user_data['password']
        response =  self.client.post(f'{version}/register',data=user_data)
        user_count = User.where_username(user_data['username']).count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(user_count, 1)
    
    # test create redundant username failed
    def test_create_user_failed(self):
        user_data = factory(User).make(username="adasdas")._attributes
        user_data['confirm_password'] = user_data['password']
        response =  self.client.post(f'{version}/register',data=user_data)

        self.assertEqual(response.status_code, 400)
    
    # test crete new user with non matching password
    def test_create_user_password_not_match(self):
        user_data = factory(User).make(username="adasdas")._attributes
        user_data['confirm_password'] = "asdkajhsdkjhd1"
        response =  self.client.post(f'{version}/register',data=user_data)

        self.assertEqual(response.status_code, 400)


class TestAuthenticate(unittest.TestCase):
    """Test user login api"""

    def setUp(self):
        self.client = app.test_client()
        self.user_data = factory(User).make(username="someuser", password="somepassword")._attributes
        try:
            self.user = User.create(self.user_data)
        except:
            pass
    
    # Test login failed with no user existence
    def test_login_failed(self):
        user_credintials = {'username': '123', 'password':'adadasd'}
        response = self.client.post(f'{version}/login', data=user_credintials)

        self.assertEqual(response.status_code, 401)

    def test_login_incorrect_password(self):
        user_credintials = {
            'username': self.user_data['username'],
            'password': "asdaskjhad"
        }
        response = self.client.post(f'{version}/login', data=user_credintials)

        self.assertEqual(response.status_code, 401)

    # test auth token missing in recipe create
    def test_auth_token_missing(self):
        recipe_data = recipe_factory(Recipe).make()._attributes
        response = self.client.post(f'{version}/recipes', data=recipe_data)

        self.assertEqual(response.status_code, 403)

    # test auth failed with invalid token
    def test_auth_failed_invalid_token(self):
        recipe_data = recipe_factory(Recipe).make()._attributes
        token_header = {'Authorization': 'Bearer sasd'}
        response = self.client.post(f'{version}/recipes', data=recipe_data, headers=token_header)

        self.assertEqual(response.status_code, 403)

if __name__ == "__main__":
    unittest.main()
