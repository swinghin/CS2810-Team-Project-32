from django.http import HttpResponse
from django.template import loader
from .models import Dish


def staff_menu(request):
    dish_list = Dish.objects.all().values()
    template = loader.get_template('restaurant/menu_staff.html')
    context = {
        'dish_list': dish_list,
    }
    return HttpResponse(template.render(context, request))


def staff_dish_details(request, id):
    dish = Dish.objects.get(dish_id=id)
    template = loader.get_template('restaurant/dish_details.html')
    context = {
        'dish': dish,
    }
    return HttpResponse(template.render(context, request))
