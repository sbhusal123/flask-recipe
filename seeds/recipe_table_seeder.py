from orator.seeds import Seeder

from recipe.models.recipe import Recipe
from factories.recipe_factory import factory

class RecipeTableSeeder(Seeder):
    """
    Writing Seeders: https://orator-orm.com/docs/0.9/seeding.html#writing-seeders
    """
    factory = factory
    def run(self):
        """
        Run the database seeds.
        """
        self.factory(Recipe, 10).create() # create 10 instance of recipe

