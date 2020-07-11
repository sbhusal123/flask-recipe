from flask_restful import reqparse
import werkzeug

class RecipeValidator:

    def __init__(self):
        self.parser = reqparse.RequestParser()
        super().__init__()
    
    def validate(self):
        self.parser.add_argument('name', required=True, help='Recipe name is required')
        self.parser.add_argument('description', required=True, help='Recipe description is required')
        self.parser.add_argument('image', required=True, type=werkzeug.datastructures.FileStorage, location='files', help='Recipe image is required')
        return self.parser.parse_args()
        