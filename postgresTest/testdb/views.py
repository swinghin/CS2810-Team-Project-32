from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'page1.html')

def index2(request):
    return render(request, 'page2.html')