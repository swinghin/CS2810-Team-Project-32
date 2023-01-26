from django.shortcuts import render
from .models import Dishes
# Create your views here.

def index(request):
    Dishes.objects.create(
        dish_name=("Pizza"),
        price=(1.5)
    )
    Dishes.objects.create(
        dish_name=("Pasta"),
        price=(1.6)
    )

    dishes_list = Dish.objects.order_by('-dish_name')

    context = {'dish_list': dish_list}

    return render (request, 'test.html', context)
