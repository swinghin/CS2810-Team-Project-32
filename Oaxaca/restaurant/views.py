from django.http import HttpResponse
from django.template import loader
#from .models import Menu

def menu(request):
  template = loader.get_template('menu.html')
  context = {
  }
  return HttpResponse(template.render(context, request))
  
#def dishInfo(request, id):
  #template = loader.get_template('dishInfo.html')
  context = {
  }
  return HttpResponse(template.render(context, request))

def test(request):
  template = loader.get_template('dishInfo.html')
  context = {
  }
  return HttpResponse(template.render(context, request))
  