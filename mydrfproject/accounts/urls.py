from django import forms
from django.urls import path
from .views import clinic_signup, clinic_login, clinic_logout,home
from . import views

urlpatterns=[
    path('',home, name='home'),
    path('signup/', clinic_signup, name='signup'),
    path('login/', clinic_login, name='login'),
    path('logout/', clinic_logout, name='logout'),
]