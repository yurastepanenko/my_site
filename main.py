from flask import Flask
from models import db
from models import (Item,
                    Category,
                    Order)
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from dotenv import load_dotenv
import os
from store_part import store_app
from auth_lib import login_manager
from session_part import session_app
from auth_models import User
from auth_part import auth_app
from admin_adapters import AdminView,ImageView
from flask_session import Session
from mail_lib import mail,send_mail
from menu_models import MenuElement

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB"]
app.secret_key = os.environ["SECRET_KEY"]
app.config["SESSION_TYPE"] = os.environ["SESSION_TYPE"]

app.config.update({"MAIL_SERVER":os.environ["MAIL_SERVER"],
                   "MAIL_PORT":os.environ["MAIL_PORT"],
                   "MAIL_USE_SSL":os.environ["MAIL_USE_SSL"],
                   "MAIL_USERNAME":os.environ["MAIL_USERNAME"],
                   "MAIL_PASSWORD":os.environ["MAIL_PASSWORD"]})
mail.init_app(app)



Session(app)

db.init_app(app)

with app.app_context():
    db.create_all()
    app.jinja_env.globals["menu_elements"] = MenuElement.query.all()
    

login_manager.init_app(app)

app.register_blueprint(store_app,url_prefix="/store")
app.register_blueprint(session_app,url_prefix="/sessions")
app.register_blueprint(auth_app,url_prefix="/auth")



admin = Admin(app, name='Магазин', template_mode='bootstrap3')
admin.add_view(ImageView(Item, db.session))
admin.add_view(ImageView(Category, db.session))
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(MenuElement, db.session))
admin.add_view(AdminView(Order, db.session))

if __name__ == "__main__":
    app.run()





