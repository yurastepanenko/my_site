from models import db
from flask_login import UserMixin

class User(db.Model,
           UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    login = db.Column(db.String(200))
    password = db.Column(db.String(400))
