from werkzeug.security import generate_password_hash, check_password_hash

def login(username, password):
    """
    Logs in a user with the given username and password.

    Args:
      username: The username of the user to log in.
      password: The password of the user to log in.

    Returns:
      A boolean value indicating whether the login was successful.
    """

    # Check if the username exists in the database.
    user = User.query.filter_by(username=username).first()
    if user is None:
        # Username does not exist
        return False

    # Check if the password is correct.
    if not check_password_hash(user.password, password):
        # Password is incorrect
        return False

    # Login successful
    return True