from django.shortcuts import render, redirect
from .models import Order
from django.template.loader import render_to_string
from .forms import OrderForm
# Create your views here.

def dashboard(request):
    orders_all = Order.objects.all()
    orders_queryset = orders_all.filter(order_finish=False)
    context = {
        "orders": orders_queryset
    }
    if request.method == "POST":
        id_list = request.POST.getlist("boxes")
        for x in id_list:
            Order.objects.filter(pk=int(x)).update(order_finish=True)
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
