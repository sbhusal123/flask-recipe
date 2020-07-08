from flask import Blueprint
from flask_restful import Resource, Api, request

from recipe.models.recipe import Recipe

from helpers.utils import recipe_exists
from orator.exceptions.query import QueryException

from recipe.api.validators.recipe_validator import RecipeValidator


class RecipeListApi(Resource):

    
    def get(self):
        recipes = Recipe.all()
        return {'data': recipes.serialize()}, 200

    def post(self):
        data = RecipeValidator().validate()
        try:
            recipe = Recipe.create(data)
        except QueryException as qe:
            return {'message': 'Recipe creation error'}, 422
        return {'data': recipe.serialize(), 'message': 'New recipe added succesfully.'}, 201
        

class RecipeApi(Resource):

    @recipe_exists
    def get(self, id):
        recipe = Recipe.find(id)
        return {'data': recipe.serialize()}, 200
    
    @recipe_exists
    def delete(self, id):
        recipe = Recipe.find(id)
        try:
            recipe.delete()
        except:
            return {'message': 'Unable to delete recipe'}, 422
        return {'message': 'Recipe deleted succesfully'}, 201

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