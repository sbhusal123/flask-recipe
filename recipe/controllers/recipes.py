from recipe.models.recipe import Recipe

def index():
    return f'- {Recipe.first().name}'