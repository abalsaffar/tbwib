from flask import Flask, request
from flask_bcrypt import Bcrypt
from your_model_module import User  # Import the User model from your module
from your_email_module import send_email  # Import the email sending function from your module
from your_otp_module import generate_otp  # Import the OTP generation function from your module

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/registration', methods=['POST'])
def registration():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    if User.query.filter_by(email=email).first() is not None:
        return 'Email already exists'

    otp = generate_otp()
    send_email(email, otp)
    user_input = input("Enter the OTP: ")

    if user_input != otp:
        return 'Incorrect OTP'

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(name=name, email=email, password=hashed_password)
    user.save()

    return 'User registered successfully'

if __name__ == '__main__':
    app.run()