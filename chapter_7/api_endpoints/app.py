from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class UserResource(Resource):
    def get(self, user_id):
        return {"user_id": user_id, "username": "exampleUser"}


api.add_resource(UserResource, "/users/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
