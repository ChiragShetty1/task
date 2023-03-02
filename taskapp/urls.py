from django.urls import path
from taskapp import views
urlpatterns = [
    path("",views.index),
    path("home",views.home),
    path("clients",views.clients),
    path("register",views.register),
    path("training",views.training),
    path("exam",views.exam)
]