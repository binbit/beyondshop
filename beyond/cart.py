import datetime
import json
from django.db import models


class CartItem(object):
    product = {}
    quantity = 0

    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity


class Cart(object):
    item_list = []

    def __init__(self, request):
        if 'cart' in request.session:
            self.cart = request.session['cart']
        else:
            self.item_list = []

    def __iter__(self):
        for item in self.cart.item_list:
            yield item

    @property
    def total_cost(self):
        total = 0
        for i in self.item_list:
            total += i.product.cost * i.quantity
        return total

    def add(self, item):
        if not(self.item_exists(item)):
            self.item_list.append(CartItem(item))

    def item_exists(self, item):
        if not(self.item_list is None):
            for i in self.item_list:
                if i.product.id == item.id:
                    return True
        return False

    def remove(self, item_id):
        for i in self.item_list:
            if i.product.id == int(item_id):
                self.item_list.remove(i)

    def clear(self):
        del self.item_list[:]

    def save(self, request):
        request.session['cart'] = self
        request.session.modified = True
