from flask_restful import reqparse

class RecipeValidator:

    def __init__(self):
        self.parser = reqparse.RequestParser()
        super().__init__()
    
    def validate(self):
        self.parser.add_argument('name', required=True, help='Recipe name is required')
        self.parser.add_argument('description', required=True, help='Recipe description is required')
        return self.parser.parse_args()
        