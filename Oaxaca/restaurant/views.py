from django.shortcuts import render
from restaurant.models import Order
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.

def showorder(request):
    orders_queryset = Order.objects.filter(order_finish=False)
    context = {
        "orders": orders_queryset
    }
    HTML_STRING = render_to_string("index.html",context=context)
    return HttpResponse(HTML_STRING)

