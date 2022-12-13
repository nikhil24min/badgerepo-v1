from django.urls import path
from . import views

urlpatterns = [
    path('index', views.homePageFunc, name="homeUrl"),
    path('register', views.registerFunc, name="registerUrl"),
    path("login", views.loginFunc, name="loginUrl"),
    path("logout", views.logoutFunc, name= "logout"),
]