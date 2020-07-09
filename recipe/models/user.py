from orator import Model


class User(Model):
    """Authentication user model"""

    __fillable__ = ['first_name', 'middle_name', 'last_name', 'username', 'password']
    
