from django.urls import path
from . import views

app_name = "restaurant"  


urlpatterns = [
    path("about/", views.about, name="about"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("accounts/login/", views.login_request, name="login"),
    path('pay/<int:id>', views.payment, name='pay'),
    path('pay/<int:id>/success/', views.payment_success, name='pay_success'),
    path('manage/menu/', views.staff_menu, name='staff-menu'),
    path('manage/menu/edit/<int:id>',
         views.staff_dish_details, name='staff-dish-details'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('orders/<int:customer_id>', views.orders, name='orders'),
    path('', views.index, name='index'),
    path('logout/', views.logout_request, name='logout'),
    path('tableManager/', views.tableManager, name="tableManager"),
    path('update_table/<str:pk>/', views.updateTable, name="update_table"),
]
