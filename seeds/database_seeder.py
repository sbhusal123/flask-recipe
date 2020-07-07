from orator.seeds import Seeder
from seeds.recipe_table_seeder import RecipeTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(RecipeTableSeeder)

