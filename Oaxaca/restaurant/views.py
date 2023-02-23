from django.shortcuts import render, redirect
from .models import *
from django.template.loader import render_to_string
from .forms import OrderForm
# Create your views here.

def dashboard(request):
    orders_all = Order.objects.all()
    customer_all = Customer.objects.all()
    help_queryset = customer_all.filter(need_help=True)
    context = {
        "orders": orders_all,
        "help": help_queryset
    }
    if request.method == "POST":
        help_list = request.POST.getlist("boxes")
        for x in help_list:
            Customer.objects.filter(pk=int(x)).update(need_help=False)
    return render(request, "dashboard.html", context=context)
  
def updateOrder(request, pk):
    order = Order.objects.get(order_id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect(dashboard)
    
    context = {'form':form}
    return render(request, "updateOrder.html", context=context)
