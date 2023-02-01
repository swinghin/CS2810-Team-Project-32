from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.test_response),
    path("login/", views.login_request)
]

