from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


item_category_table = db.Table("item_category_table",
                               db.Column("category_id",db.ForeignKey("categories.id")),
                               db.Column("item_id",db.ForeignKey("items.id"))
                               )


item_order_table = db.Table("item_order_table",
                            db.Column("order_id",db.ForeignKey("orders.id")),
                            db.Column("item_id",db.ForeignKey("items.id"))
                            )


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(250))
    items = db.relationship("Item",
                            secondary=item_category_table,
                            back_populates="categories",
                            lazy="dynamic")
    img = db.Column(db.String(150))

    def __str__(self):
        return self.name
    

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(250))
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime)
    categories = db.relationship("Category",
                                 secondary=item_category_table,
                                 back_populates="items")
    img = db.Column(db.String(150))

    def create_message_text(self):
        message = f"""Назва товару: {self.name}
Ціна товару: {self.price}"""
        return message

    
    def __str__(self):
        return self.name


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(150))
    phone = db.Column(db.String(30))
    email = db.Column(db.String(250))
    price = db.Column(db.Float())
    items = db.relationship("Item",
                            secondary=item_order_table)

    def create_message_text(self):
        message = f"""Замовлення оформив: {self.name}
Телефон замовника: {self.phone}
Емейл замовника: {self.email}
Ціна замовлення: {self.price}\n"""
        message += "Придбані товари \n"

        for item in self.items:
            message += f"{item.create_message_text()}\n"
            message += f"{'-'*20}\n"
        return message


    

