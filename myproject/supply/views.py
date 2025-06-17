from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from . import views
from django.urls import include, path

#create views
def home(request):
    return render(request, "supply/home.html")

# Create your views here.
