from models import db

class MenuElement(db.Model):
    __tablename__ = "menu_elements"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(150))
    link = db.Column(db.String(250))
