from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.


def index(request):
    for i in range(5):
        Employee.objects.create(
            employee_name=("Employee "+str(Employee.objects.count()+1)))
    return HttpResponse(Employee.objects.all())
