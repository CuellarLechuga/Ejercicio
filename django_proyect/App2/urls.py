from django.urls import path
from . import views

urlpaterns = [
    path("", views.home, name = "Inicio"),
   # path("about/", views.about, name = "Acera de"),
   # path("menu/", views.menu, name = "Menu"),
]