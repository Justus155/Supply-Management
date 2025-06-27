from django import forms
from django.urls import path
from .views import clinic_signup, clinic_login, clinic_logout,home
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import views

urlpatterns=[
    path('',home, name='home'),
    #signup and login views
    path('clinic_signup/', views.clinic_signup_view, name='clinic_signup'),
    path('clinic_login/', views.clinic_login_view, name='clinic_login'),
    #mydrf urls
    path('signup/', clinic_signup, name='signup'),
    path('login/', clinic_login, name='login'),
    path('logout/', clinic_logout, name='logout'),
]