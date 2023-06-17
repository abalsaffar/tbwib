# Import necessary modules from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# Initialize a SQLAlchemy object
db = SQLAlchemy()

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    name = db.Column(db.String(255), nullable=False)  # User's name
    email = db.Column(db.String(255), nullable=False, unique=True)  # User's email, must be unique
    password = db.Column(db.String(255), nullable=False)  # User's hashed password

# Define the Category model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each category
    name = db.Column(db.String(255), nullable=False, unique=True)  # Category name, must be unique

# Define the SubCategory model
class SubCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each subcategory
    name = db.Column(db.String(255), nullable=False)  # Subcategory name
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)  # Foreign key linking subcategory to its category
    category = db.relationship('Category', backref=db.backref('subcategories', lazy=True))  # Relationship between Category and SubCategory models

# Define the Content model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each content item
    title = db.Column(db.String(255), nullable=False)  # Content title
    description = db.Column(db.Text, nullable=False)  # Content description
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key linking content to its author (a user)
    author = db.relationship('User', backref=db.backref('contents', lazy=True))  # Relationship between User and Content models
    subcategory_id = db.Column(db.Integer, db.ForeignKey('sub_category.id'), nullable=False)  # Foreign key linking content to its subcategory
    subcategory = db.relationship('SubCategory', backref=db.backref('contents', lazy=True))  # Relationship between SubCategory and Content models