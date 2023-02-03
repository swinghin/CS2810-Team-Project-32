from django.shortcuts import render
from restaurant.models import Order
from django.template.loader import render_to_string
# Create your views here.

def showorder(request):
    orders_all = Order.objects.all()
    orders_queryset = orders_all.filter(order_finish=False)
    context = {
        "orders": orders_queryset
    }
    if request.method == "POST":
        id_list = request.POST.getlist("boxes")
        for x in id_list:
            Order.objects.filter(pk=int(x)).update(order_finish=True)
    return render(request, "index.html", context=context)
  

