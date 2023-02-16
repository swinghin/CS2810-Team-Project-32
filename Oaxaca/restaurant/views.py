from django.http import HttpResponse
from django.template import loader
from .models import Dish

def menu(request):
  dish = Dish.objects.all().values()
  template = loader.get_template('menu.html')
  context = {
    'dish': dish,
  }
  return HttpResponse(template.render(context, request))
  

def details(request, id):
  dish = Dish.objects.get(dish_id=id)
  template = loader.get_template('details.html')
  context = {
    'dish': dish,
  }
  return HttpResponse(template.render(context, request))

  