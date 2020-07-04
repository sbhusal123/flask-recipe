from app.models import db

class User(db.Model):

    __fillable__ = ['name', 'email']

    def __repr__(self):
        return f'<User {}>'.format(self.name)

