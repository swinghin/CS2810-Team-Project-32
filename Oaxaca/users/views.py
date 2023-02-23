from django.shortcuts import render
from django.views import View
from restaurant.models import Order

# Create your views here.

class DashboardWaiter(View):
    def get(self, request, *args, **kwargs):
        all_orders = Order.objects.all()
        orders_ready = [order for order in all_orders if order.status == 'ready']
        orders_not_ready = [order for order in all_orders if order.status != 'ready']
        context = {
            'all_orders': all_orders,
            'orders_ready': orders_ready,
            'orders_not_ready': orders_not_ready,
        }
        
        return render(request, 'users/dashboard_waiter.html', context)
