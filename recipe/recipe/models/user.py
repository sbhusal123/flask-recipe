from orator import Model
from orator import mutator

import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash


class User(Model):
    """Authentication user model"""

    __fillable__ = ['first_name', 'middle_name', 'last_name', 'username', 'password']

    @mutator
    def password(self, password):
        """Create hashed password."""
        hashed_password = generate_password_hash(
            password,
            method='sha256'
        )
        self.set_raw_attribute('password', str(hashed_password))
