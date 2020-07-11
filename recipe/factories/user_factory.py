from orator.orm import Factory
from recipe.models.user import User

factory = Factory()

@factory.define(User)
def user_factory(faker):
    return {
        'first_name': faker.first_name(),
        'middle_name': faker.word(),
        'last_name': faker.last_name(),
        'username': faker.name(),
        'password': faker.password()
    }