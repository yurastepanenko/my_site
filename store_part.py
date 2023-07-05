from flask import (Blueprint,
                   render_template,
                   session,
                   redirect,
                   url_for,
                   request)

from models import Item,Category
from cart import init_cart
from models import db
from forms import OrderForm
from mail_lib import send_mail
import os

store_app = Blueprint('store_app', __name__,
                      template_folder='templates')


@store_app.route("/")
def view_items():
    items = db.paginate(db.select(Item),per_page=16)
    return render_template("items.html",
                           items=items)

@store_app.route("/<int:item_id>")
def view_item(item_id):
    item = Item.query.filter(Item.id == item_id).first()
    return render_template("item.html",
                           item=item)

@store_app.route("/categories")
def view_categories():
    categories = Category.query.all()
    return render_template("categories.html",
                    categories=categories)

@store_app.route("/categories/<int:category_id>")
def view_category(category_id):
    
    category = Category.query.filter(Category.id == category_id).first()
    items = db.paginate(category.items,per_page=16)
    return render_template("category.html",
                           category=category,
                           items=items)



@store_app.route("/cart")
def view_cart():
    init_cart(session)
    cart = session.get("cart")
    return render_template("cart.html",
                           cart=cart)

@store_app.route("/add_to_cart/<int:item_id>")
def add_to_cart(item_id):
    init_cart(session)
    cart = session.get("cart")
    item = Item.query.filter(Item.id==item_id).first()
    if item:
        cart.add_item(item)
    return redirect(url_for("store_app.view_cart"))


@store_app.route("/clear_cart")
def clear_cart():
    init_cart(session)
    cart = session.get("cart")
    cart.clear()
    return redirect(url_for("store_app.view_cart"))


@store_app.route("/create_order",methods=["GET","POST"])
def create_order():
    init_cart(session)
    form = OrderForm()
    if request.method == "POST":
        cart = session.get("cart")
        if cart.items:
            form_data = request.form
            order = cart.create_order(form_data)
            db.session.add(order)
            db.session.commit()
            cart.clear()
            send_mail(title="Замовлення на сайті",
                      body=order.create_message_text(),
                      recipients=["egen13@ukr.net"])

            return render_template("thank.html")
        
    return render_template("order.html",
                           form=form,
                           cart=session.get("cart"))

   

    
