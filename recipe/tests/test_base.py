import unittest
from recipe import app
from recipe.models.user import User

from factories.user_factory import factory
from . import version

import json


class TestBase(unittest.TestCase):
    """Base class for all test cases requiring user token"""

    token_header = None

    def setUp(self):
        # Create Login User
        user_data = {"username":"fakerFilla!!","password":"faker"}
        try:
            user = factory(User).create(**user_data)
        except Exception as e:
            pass

        # Login and get token
        response = app.test_client().post(f'{version}/login', data=user_data)
        json_data = json.loads(response.data)
        token = json_data['token']
        self.token_header = {'Authorization': f'Bearer {token}'}