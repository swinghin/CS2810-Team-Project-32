from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import Dish
from .forms import DishForm


def staff_menu(request):
    dish_list = Dish.objects.all().order_by('dish_name').values()
    template = loader.get_template('restaurant/menu_staff.html')
    context = {
        'dish_list': dish_list,
    }
    return HttpResponse(template.render(context, request))


def staff_dish_details(request, id):
    dish = Dish.objects.get(dish_id=id)

    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('staff-menu')

    else:
        template = loader.get_template('restaurant/dish_details.html')
        form = DishForm(instance=dish)
        context = {
            'dish': dish,
            'form': form
        }
    return HttpResponse(template.render(context, request))
