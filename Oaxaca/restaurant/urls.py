from django.urls import path
from . import views

app_name = "restaurant"   


urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("home/", views.redirect_request, name="homepage"),
    path("login/", views.login_request, name="login")
]