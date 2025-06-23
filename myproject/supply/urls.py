from django.urls import path
from django.shortcuts import render
from django.urls import include, path
from .import views


urlpatterns = [
    path("", views.home, name='supply-home'),
    path('signIn/', views.signIn, name='supply-signin'),
    path('signUp/', views.SignUp, name='supply-signup'),
]