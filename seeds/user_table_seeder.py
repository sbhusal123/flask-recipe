from orator.seeds import Seeder
from factories.user_factory import factory
from recipe.models.user import User


class UserTableSeeder(Seeder):

    factory = factory

    def run(self):
        """
        Run the database seeds.
        """
        self.factory(User, 5).create()

