from flask import Blueprint
from flask_restful import Resource, Api, request

from recipe.models.recipe import Recipe

from helpers.utils import recipe_exists
from orator.exceptions.query import QueryException

from auth_encryption.authentication import auth
from recipe.api.validators.recipe_validator import RecipeValidator

from werkzeug.utils import secure_filename
import os
from recipe import app

class RecipeListApi(Resource):


    def get(self):
        recipes = Recipe.all()
        return {'data': recipes.serialize()}, 200

    @auth
    def post(self):
        data = RecipeValidator().validate()

        # Upload files
        image = data.image
        image_filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
        try:
            image.save(image_path)
        except Exception as e:
            print(e)
            print(image_path)
            return {'message': 'Unale to upload file.'}, 422
        data.pop('image')

        try:
            recipe = Recipe.create(data, image=image_filename)
        except QueryException as qe:
            return {'message': 'Recipe creation error'}, 422
        return {'data': recipe.serialize(), 'message': 'New recipe added succesfully.'}, 201
        

class RecipeApi(Resource):

    @recipe_exists
    def get(self, id):
        recipe = Recipe.find(id)
        return {'data': recipe.serialize()}, 200
    
    @auth    
    @recipe_exists
    def delete(self, id):
        recipe = Recipe.find(id)
        try:
            recipe.delete()
        except:
            return {'message': 'Unable to delete recipe'}, 422
        return {'message': 'Recipe deleted succesfully'}, 201

    @auth
    @recipe_exists
    def put(self, id):
        recipe = Recipe.find(id)
        data = request.form
        try:
            recipe.update(data)
        except:
            return {'message': 'Unable to update recipe'}, 422
        return {'message': 'Recipe updated succesfully', 'data': recipe.serialize()}, 201

recipe_api = Blueprint('recipe.api.recipe', __name__)
api = Api(recipe_api)

api.add_resource(RecipeListApi, '/recipes',endpoint="recipes")
api.add_resource(RecipeApi,'/recipe/<int:id>',endpoint="recipe")