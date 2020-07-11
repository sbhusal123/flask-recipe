from recipe.models.recipe import Recipe

from orator.exceptions.orm import ModelNotFound
 
import PIL.Image
import tempfile

from functools import wraps
import pathlib
import uuid
import os


def recipe_exists(func):
    """Check if recipe with id exists.If exists procede else return 404"""
    @wraps(func)
    def inner_function(self, *args, **kwargs):
        try:
            Recipe.where('id', kwargs['id']).first_or_fail()
        except ModelNotFound:
            return {'message': 'Recipe not found'}, 404
        return func(self, *args, **kwargs)
    return inner_function

def unique_file_name(filename):
    """Generate uniqie file name"""
    # Get storage path
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

def create_test_image():
    """Generate temporary test image file"""
    image = PIL.Image.new('RGB', size=(100, 100))
    file = tempfile.NamedTemporaryFile(suffix='.jpg')
    image.save(file)
    return file