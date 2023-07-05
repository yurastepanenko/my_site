from wtforms_alchemy import ModelForm
from models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['price']
