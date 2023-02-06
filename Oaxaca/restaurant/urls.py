from django.urls import path
from . import views

app_name = "restaurant"   


urlpatterns = [
    path("register/", views.register_request),
    path("home/", views.redirect_request, name="homepage")
]