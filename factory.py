from main import app
from models import db
from auth_models import User
import random
from models import Item
users = [{"login":"admin",
          "password":"123123"}]


def create_users():
    for user in users:
        db.session.add(User(login=user["login"],
                            password=user["password"]))
    db.session.commit()


def create_items(count):
    for number in range(count):
        item = Item(name=f"Item {number}",
                    description = f"Description {number}",
                    price = random.randint(10,100000))
        db.session.add(item)
    db.session.commit()
    

with app.app_context():
    create_items(400)
