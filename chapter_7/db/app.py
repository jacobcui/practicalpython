from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import names
import random


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
db = SQLAlchemy(app)
api = Api(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)


# Create the table
with app.app_context():
    db.create_all()


class AllUsers(Resource):
    def get(self):
        user_data = []
        for u in db.session.query(User).all():
            user_data.append({"id": u.id, "name": u.name, "age": u.age})
        return user_data


class UserResource(Resource):
    def get(self, user_id):
        if u := db.session.query(User).get(user_id):
            user_data = {"id": u.id, "name": u.name, "age": u.age}
        else:
            user_data = {"error": f"Cannot find user by id {user_id}."}
        return user_data


# Create a user
with app.app_context():
    new_user = User(name=names.get_full_name(), age=random.randint(1, 90))
    db.session.add(new_user)
    db.session.commit()

api.add_resource(AllUsers, "/users")
api.add_resource(UserResource, "/users/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
