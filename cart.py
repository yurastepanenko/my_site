from models import Order

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        if item.id not in [item.id for item in self.items]:
            self.items.append(item)
        
    def clear(self):
        self.items.clear()

    def count(self):
        return len(self.items)

    def get_price(self):
        price = 0
        for item in self.items:
            price += item.price
        return price
    
    def create_order(self,form_data):
        order = Order(name=form_data.get("name"),
                      email=form_data.get("email"),
                      phone=form_data.get("phone"),
                      price=self.get_price())
        for item in self.items:
            order.items.append(item)
        return order
        


def init_cart(session):
    if "cart" not in session:
        session["cart"] = Cart()


# Додати товар

# Очистити товари

# Визначити вартість товарів

# Кількість товарів в корзині
