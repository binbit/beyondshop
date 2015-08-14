class Cart(object):
    item_list = []

    def __init__(self, request):
        if 'cart' in request.session:
            self.item_list = request.session['cart']
        else:
            self.item_list = []

    def __iter__(self):
        for item in self.item_list:
            yield item

    def add(self, item):
        if not(self.item_exists(item)):
            self.item_list.append(item.id)

    def item_exists(self, item):
        if not(self.item_list is None):
            for i in self.item_list:
                if i == item.id:
                    return True
        return False

    def remove(self, item_id):
        for i in self.item_list:
            if i == int(item_id):
                self.item_list.remove(i)

    def clear(self):
        del self.item_list[:]

    def save(self, request):
        request.session['cart'] = self.item_list
        request.session.modified = True
