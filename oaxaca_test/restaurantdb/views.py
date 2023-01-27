from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Dish

# Create your views here.


def index(request):
    # Dish.objects.create(
    #     dish_name=("Fish and Crisps"),
    #     price=(6.90)
    # )
    # Dish.objects.create(
    #     dish_name=("Snoopy Hot Dogg"),
    #     price=(4.20)
    # )

    dish_list = Dish.objects.order_by('-dish_name')
    context = {
        'dish_list': dish_list
    }
    return render(request, 'restaurantdb/index.html', context)


def menu(request):
    # Dish.objects.create(
    #     dish_name=("Fish and Crisps"),
    #     price=(6.90)
    # )
    # Dish.objects.create(
    #     dish_name=("Snoopy Hot Dogg"),
    #     price=(4.20)
    # )

    dish_list = Dish.objects.order_by('-dish_name')
    context = {
        'dish_list': dish_list
    }
    return render(request, 'restaurantdb/menu.html', context)


def cart(request, table=-1):

    order_list = Dish.objects.order_by('-price')[:2]

    total = 0.0
    for order in order_list:
        total += float(order.price)

    context = {
        'order_list': order_list,
        'price_total': total
    }

    return render(request, 'restaurantdb/cart.html', context)
