from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manage/menu/', views.staff_menu, name='staff-menu'),
    path('manage/menu/edit/<int:id>',
         views.staff_dish_details, name='staff-dish-details'),
]