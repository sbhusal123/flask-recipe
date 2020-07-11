from flask import Blueprint
from .recipes import index as recipeIndex

recipe = Blueprint('recipe', __name__, url_prefix='/recipes')
recipe.add_url_rule('', view_func=recipeIndex)