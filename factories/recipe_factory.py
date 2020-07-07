from orator.orm import Factory
from recipe.models.recipe import Recipe

factory = Factory()

# Overloading with Decorator
@factory.define(Recipe)
def recipe_factory(faker):
    return {
        'name': faker.word(),
        'description': faker.text()
    }