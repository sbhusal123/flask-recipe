from flask_restful import reqparse

class LoginValidator():
    def __init__(self):
        self.parser = reqparse.RequestParser()
    
    def validate(self):
        self.parser.add_argument('username', required=True, help="Username is required.")
        self.parser.add_argument('password', required=True, help="Password is required.")
        return self.parser.parse_args()


class RegisterValidator():
    def __init__(self):
        self.parser = reqparse.RequestParser()
    
    def validate(self):
        self.parser.add_argument('first_name', required=True, help="First name is required.")
        self.parser.add_argument('middle_name', required=False)
        self.parser.add_argument('last_name', required=True, help="Last name is required.")
        self.parser.add_argument('username', required=True, help="Username name is required.")
        self.parser.add_argument('password', required=True, help="Password is required.")
        self.parser.add_argument('confirm_password', required=True, help="Confirmation Password is required.")
        
        return self.parser.parse_args()
