from . import db
from flask_login import UserMixin


# Define a User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

# Define a Image model
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(80), unique=True, nullable=False)
    image_url = db.Column(db.String(256), unique=True, nullable=False)
    likes = db.Column(db.Integer)


    def __init__(self, userid, image_url, likes):
        self.userid = userid
        self.image_url = image_url
        self.likes = likes

# Define a PhotoComment model
class PhotoComment(db.Model):
    userid = db.Column(db.Integer, nullable=False)
    photoid = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(1024), nullable=False)

    def __init__(self, userid, photoid, comment):
        self.userid = userid
        self.photoid = photoid
        self.comment = comment

# Define a PhotoFeed model
class PhotoFeed(db.Model):
    userid = db.Column(db.Integer, nullable=False)
    photoid = db.Column(db.Integer, nullable=False)

    def __init__(self, userid, photoid):
        self.userid = userid
        self.photoid = photoid
