from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login_manager



class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    user_password = db.Column(db.String,unique=True,nullable=False)
    pitches = db.relationship('Pitch',backref='pitch',lazy='dynamic')
    comments = db.relationship('Comments', backref='user', lazy='dynamic') 

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()


    def verify_password(self, password):
        return check_password_hash(self.user_password, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @property
    def password(self):
        raise AttributeError('Error')
        
    @password.setter
    def password(self,password):
        self.user_password= generate_password_hash(password)



    def __repr__(self):
        return f"{self.username}"

class Category(db.Model):
    __tablename__='category'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return f"Category {self.name} " 

class Pitch(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content =db.Column(db.Text,nullable=False)
    author = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    category = db.Column(db.String,default='general')
    comments = db.relationship('Comments',backref='pitches', lazy='dynamic')
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()    


class Votes(db.Model):
    __tablename__='votes'
    id = db.Column(db.Integer,primary_key=True)
    down_votes = db.Column(db.Integer)
    up_votes = db.Column(db.Integer)

class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key=True)
    content =db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable=False)
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
