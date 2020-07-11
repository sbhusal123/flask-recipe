import unittest
import json
from .test_base import TestBase

from . import version
from recipe import app
from recipe.models.recipe import Recipe
from factories.recipe_factory import factory

from helpers.utils import create_test_image
from orator.exceptions.orm import ModelNotFound

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
    
    # Test get specific recipe success
    def test_get_recipe(self):
        recipe = factory(Recipe).create()
        response = self.client.get(f'{version}/recipe/{recipe.id}')
        json_response = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(recipe.serialize(),json_response['data'])

    # Test get non existing recipe
    def test_get_recipe_not_found(self):
        recipe = factory(Recipe).create()
        response = self.client.get(f'{version}/recipe/10000')
        
        self.assertEqual(response.status_code, 404)
    
    # test update recipe with valid data success
    def test_update_recipe(self):
        recipe = Recipe.first()
        recipe_data = {'name': 'new_name'}
        response = self.client.put(f'{version}/recipe/{recipe.id}', headers=self.token_header, data=recipe_data)
        json_response = json.loads(response.data)

        self.assertEqual(recipe_data['name'], json_response['data']['name'])
        self.assertEqual(response.status_code, 201)
    
    # test update recipe with redundant name
    def test_update_recipe_failed(self):
        first_item = Recipe.first()
        recipe_data = {'name': 'Failed Name'}
        recipe = factory(Recipe).create(**recipe_data)
        response = self.client.put(f'{version}/recipe/{first_item.id}', headers=self.token_header, data=recipe_data)
        
        self.assertEqual(response.status_code, 422)

    # test delete_recipe_succesfull
    def test_delete_recipe(self):
        recipe = Recipe.first()
        response = self.client.delete(f'{version}/recipe/{recipe.id}', headers=self.token_header)
        
        self.assertEqual(response.status_code, 201)
        with self.assertRaises(ModelNotFound):
            Recipe.where_id(recipe.id).first_or_fail()

if __name__ == "__main__":
    unittest.main()
