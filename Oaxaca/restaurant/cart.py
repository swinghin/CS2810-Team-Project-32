from django.conf import settings

from restaurant.models import Customer, Dish, Order

class Cart(obj):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
    
    def list_cart(self):
        for d in self.cart.keys():
            self.cart[str(d)]['Dish'] = Dish.objects.get(pk = d)

    def add_item(self, dish_id, quantity = 1, update_quantity=False):
        dish_id = str(dish_id)

        if dish_id not in self.cart:
            self.cart[dish_id] = {'quantity': 1, 'id': dish_id}

        if update_quantity:
            self.cart[dish_id]['quantity'] += int(quantity)

            if self.cart[dish_id]['quantity'] == 0:
                self.remove(dish_id)

    def remove_item(self, dish_id):
        if dish_id in self.cart:
            del self.cart[dish_id]
            self.save_cart()

    def save_cart(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True