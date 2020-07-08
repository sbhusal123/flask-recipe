from recipe.models.recipe import Recipe

from orator.exceptions.orm import ModelNotFound

from functools import wraps
import uuid



def recipe_exists(func):
    """Check if recipe with id exists.If exists procede else return 404"""
    @wraps(func)
    def inner_function(self, *args, **kwargs):
        try:
            Recipe.where('id', kwargs['id']).first_or_fail()
        except ModelNotFound:
            return {'message': 'Recipe not found',}, 404
        return func(self, *args, **kwargs)
    return inner_function
