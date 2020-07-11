from orator.migrations import Migration


class CreateUserTable(Migration):

    def up(self):
        with self.schema.create('users') as table:
            table.big_increments('id')
            table.string('first_name')
            table.string('middle_name').nullable()
            table.string('last_name')
            table.string('username',25).uniqie()
            table.string('password')
            table.timestamps()
        pass

    def down(self):
        self.schema.drop('users')
        pass
