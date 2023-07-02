# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api, Resource
from models import db, User, Category, SubCategory, Content
from user_utils import password_reset

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tbwib.com:Mv39dk123456@@localhost/sqxblpmy_WP45H'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

api = Api(app)

class PasswordResetResource(Resource):
    def post(self):
# ... (same as before)

api.add_resource(PasswordResetResource, '/password-reset')

class RegisterResource(Resource):
    def post(self):
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        user.send_verification_email()

        return {'message': 'User registered successfully'}

api.add_resource(RegisterResource, '/register')

class VerifyCodeResource(Resource):
    def post(self):
        code = request.form['code']

        user = User.query.filter_by(code=code).first()
        if user:
            user.verified = True
            db.session.commit()

            return {'message': 'Code verified successfully'}
        else:
            return {'message': 'Code invalid'}

api.add_resource(VerifyCodeResource, '/verify-code')

class LoginResource(Resource):
    def post(self):
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return {'message': 'User logged in successfully', 'id': user.id}
        else:
            return {'message': 'Invalid credentials'}

api.add_resource(LoginResource, '/login')

class LogoutResource(Resource):
    def post(self):
        user_id = request.form['id']

        user = User.query.get(user_id)
        user.logout()
        db.session.commit()

        return {'message': 'User logged out successfully'}

api.add_resource(LogoutResource, '/logout')

if __name__ == '__main__':
    app.run(debug=True)
