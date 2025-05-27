from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
#from .models import Menu


# Create your views here.
def home(request):
    contexto = {}
    return render(request, "home.html", contexto)
