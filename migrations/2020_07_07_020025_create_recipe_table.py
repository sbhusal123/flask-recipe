from orator.migrations import Migration


class CreateRecipeTable(Migration):
    """
    Writing migrations: https://orator.readthedocs.io/en/latest/migrations.html
    """

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('recipes') as table:
            table.increments('id')
            table.string('name')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('recipes')
