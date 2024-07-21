from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///crud_app.db"  # Using SQLite for simplicity
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Initialize Flask-RESTful API
api = Api(app)


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the user
    name = db.Column(db.String(50))  # User's name
    age = db.Column(db.Integer)  # User's age

    # Method to convert User object to a dictionary
    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age}


# Create the table in the database
with app.app_context():
    db.create_all()


# Define the UserResource class for handling user-related operations
class UserResource(Resource):
    # GET method to retrieve users
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)  # Retrieve user by ID
            if user:
                return jsonify(user.to_dict())  # Return user as JSON
            else:
                return {
                    "message": "User not found"
                }, 404  # Return 404 if user not found
        else:
            users = User.query.all()  # Retrieve all users
            return jsonify(
                [user.to_dict() for user in users]
            )  # Return all users as JSON

    # POST method to create a new user
    def post(self):
        data = request.get_json()  # Get JSON data from the request
        new_user = User(name=data["name"], age=data["age"])  # Create new user object
        db.session.add(new_user)  # Add new user to the session
        db.session.commit()  # Commit the session to save the new user
        return jsonify(new_user.to_dict())  # Return the new user as JSON

    # PUT method to update an existing user
    def put(self, user_id):
        data = request.get_json()  # Get JSON data from the request
        user = User.query.get(user_id)  # Retrieve user by ID
        if user:
            if new_name := data.get("name"):  # Update name if provided
                user.name = new_name
            if new_age := data.get("age"):  # Update age if provided
                user.age = new_age
            db.session.commit()  # Commit the session to save the changes
            return jsonify(user.to_dict())  # Return the updated user as JSON
        else:
            return {"message": "User not found"}, 404  # Return 404 if user not found

    # DELETE method to delete a user
    def delete(self, user_id):
        user = User.query.get(user_id)  # Retrieve user by ID
        if user:
            db.session.delete(user)  # Delete the user from the session
            db.session.commit()  # Commit the session to delete the user
            return {"message": "User deleted"}  # Return success message
        else:
            return {"message": "User not found"}, 404  # Return 404 if user not found


# Add the UserResource to the API with routes for handling users
api.add_resource(UserResource, "/users", "/users/<int:user_id>")

# Run the Flask app if this script is the main program
if __name__ == "__main__":
    app.run(debug=True)
