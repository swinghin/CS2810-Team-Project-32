from django.shortcuts import render
from .models import Dishes
# Create your views here.

def index(request):
    dishes_list = Dish.objects.order_by('-dish_name')

    context = {'dish_list': dish_list}

    return render (request, 'test.html', context)
