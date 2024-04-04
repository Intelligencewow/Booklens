from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("", views.homepage, name="index"),  
    path("plataforma/", views.plataforma, name="plataforma")
]