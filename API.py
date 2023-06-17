from flask import Flask

app = Flask(__name__)

from .users import users

@app.route('/users', methods=['POST'])
def register_user():
    """
    This function registers a new user.

    Returns:
        json: A JSON response with the user object.
    """

    # Get the user's name, email, and password from the request body.
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    # Create a new user object.
    user = User(name=name, email=email, password=password)

    # Add the user to the database.
    db.session.add(user)

    # Commit the changes to the database.
    db.session.commit()

    # Return a JSON response with the user object.
    return jsonify({'user': user})

@app.route('/users/login', methods=['POST'])
def login_user():
    """
    This function logs in a user.

    Returns:
        json: A JSON response with the user object.
    """

    # Get the user's email and password from the request body.
    email = request.json['email']
    password = request.json['password']

    # Get the user from the database by the user's email address.
    user = User.query.filter_by(email=email).first()

    # If the user exists and the password is correct, return the user object.
    if user and user.check_password(password):
        return jsonify({'user': user})

    # Otherwise, return a JSON response with an error message.
    else:
        return jsonify({'error': 'Invalid credentials'})

@app.route('/users', methods=['GET'])
def get_users():
    """
    This function gets all users.

    Returns:
        json: A JSON response with all users.
    """

    # Get all users from the database.
    users = User.query.all()

    # Return a JSON response with all users.
    return jsonify({'users': users})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    This function gets a single user by the user's ID.

    Args:
        user_id: The ID of the user to get.

    Returns:
        json: A JSON response with the user object.
    """

    # Get the user from the database by the user's ID.
    user = User.query.get(user_id)

    # Return a JSON response with the user object.
    return jsonify({'user': user})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    This function updates a user in the database.

    Args:
        user_id: The ID of the user to update.

    Returns:
        json: A