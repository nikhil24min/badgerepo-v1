from django.urls import path
from . import views

urlpatterns = [
    path('index', views.homePageFunc, name="homeUrl"),
    path('register', views.registerFunc, name="registerUrl"),
    path("login", views.loginFunc, name="loginUrl"),
    path("logout", views.logoutFunc, name= "logout"),

    path("addbadge", views.addBadgeFunc, name="addBadgeUrl"),
    path("displaybadge/<int:pkid>", views.displayBadgeFunc, name="displayBadgeUrl"),
    path("deletebadge/<int:pkid>", views.deleteBadgeFunc, name="deleteBadgeUrl"),
]