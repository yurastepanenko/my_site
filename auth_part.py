from flask import Blueprint,render_template,request,redirect
from auth_models import User
from flask_login import (login_user,
                         logout_user)
from flask_login import current_user


auth_app = Blueprint('auth_app', __name__,
                     template_folder='templates')


@auth_app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        form_data = request.form
        user = User.query\
               .filter(User.login == form_data.get("login"))\
               .filter(User.password == form_data.get("password"))\
               .first()
        if user:
            login_user(user)
            return redirect("/admin")
    return render_template("login.html")


@auth_app.route("/logout")
def logout():
    logout_user()
    return "Ви Вийшли"

@auth_app.route("/get_user")
def get_user():
    if current_user:
        return current_user.login
    else:
        return "Не увійшли"

