from orator.seeds import Seeder
from seeds.recipe_table_seeder import RecipeTableSeeder
from seeds.user_table_seeder import UserTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(RecipeTableSeeder)
        self.call(UserTableSeeder)

