from django.urls import path
from . import views

app_name = "restaurant"  


urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("home/", views.redirect_request, name="homepage"),
    path("login/", views.login_request, name="login"),
    path('pay/', views.payment, name='pay'),
    path('manage/menu/', views.staff_menu, name='staff-menu'),
    path('manage/menu/edit/<int:id>',
         views.staff_dish_details, name='staff-dish-details'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('', views.index, name='index'),
    path('waiter/', views.waiter_view, name='waiter_page'),
    path('logout/', views.logout_request, name='logout')
]
