from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    notes = db.relationship('Note')

class Song(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    video = db.Column(db.String(100), unique=True)
    game = db.Column(db.String(100))
    joke = db.Column(db.String(100))
    # joke_id = db.Column(db.Integer, db.ForeignKey('joke.id'))

# class Joke(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     joke = db.Column(db.String(255))

