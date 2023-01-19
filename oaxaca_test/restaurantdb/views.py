from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee

# Create your views here.


def index(request):
    # for i in range(5):
    #     Employee.objects.create(
    #         employee_name=("Employee "+str(Employee.objects.count()+1)))
    employee_list = Employee.objects.order_by('-id')
    context = {
        'employee_list': employee_list
    }
    return render(request, 'restaurantdb/index.html', context)
