from django.urls import path
from . import views

app_name = "restaurant"   


urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("home/", views.redirect_request, name="homepage"),
    path("login/", views.login_request, name="login"),
    path('pay/', views.payment, name='pay'),
    path('', views.index, name='index'),
    path('manage/menu/', views.staff_menu, name='staff-menu'),
    path('manage/menu/edit/<int:id>',
         views.staff_dish_details, name='staff-dish-details'),
]