import unittest
import json
from .test_base import TestBase

from . import version
from recipe import app
from recipe.models.recipe import Recipe
from factories.recipe_factory import factory

from helpers.utils import create_test_image

class TestRecipe(TestBase):
    """Test user authentication"""


    def setUp(self):
        super().setUp()
        self.client = app.test_client()
    
    # Get recipe list
    def test_get_recipe_list(self):
        response = self.client.get(f'{version}/recipes')
        json_response = json.loads(response.data)
        recipe_data = Recipe.all().serialize()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response['data'], recipe_data)
    
    # post new recipe
    def test_create_new_recipe(self):
        recipe_data = factory(Recipe).make()._attributes
        recipe_image = create_test_image()
        with open(recipe_image.name, 'rb') as image_file:
            recipe_data['image'] = image_file
            response = self.client.post(f'{version}/recipes', headers=self.token_header, data=recipe_data)
            self.assertEqual(response.status_code, 201)
    
    # Test that creating recipe with duplicate name fails
    def test_create_duplicae_recipe_name(self):
        recipe = {'name': 'Fake Recipe'}
        factory(Recipe).create(**recipe)
        recipe_image = create_test_image()

        # Using file in post request
        with open(recipe_image.name, 'rb') as image_file:
            recipe_data = factory(Recipe).make(**recipe)._attributes
            recipe_data['image'] = image_file
            response = self.client.post(f'{version}/recipes', headers=self.token_header, data=recipe_data)
            self.assertEqual(response.status_code, 422)



if __name__ == "__main__":
    unittest.main()
