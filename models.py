from sqlalchemy import Boolean, Column, Integer, String

class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    verified = Column(Boolean, default=False)
    code = Column(String(255))

    def __repr__(self):
        return '<User id={id}, name={name}, email={email}, verified={verified}>'.format(
            id=self.id,
            name=self.name,
            email=self.email,
            verified=self.verified,
        )

class Category(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

class SubCategory(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    category_id = Column(Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('subcategories', lazy=True))

class Content(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    user_id = Column(Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref=db.backref('contents', lazy=True))
    subcategory_id = Column(Integer, db.ForeignKey('subcategory.id'), nullable=False)
    subcategory = db.relationship('SubCategory', backref=db.backref('contents', lazy=True))
