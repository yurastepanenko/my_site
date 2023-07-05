from flask import Blueprint,render_template

session_app = Blueprint('session_app', __name__,
                        template_folder='templates')


@session_app.route("/")
def view_session():
    return render_template("view_sessions.html")
