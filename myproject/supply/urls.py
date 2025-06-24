from django.urls import path
from django.shortcuts import render
from django.urls import include, path
from django.http import HttpResponse
from django.contrib.auth import login
from .models import clinicSignIn, DistributorSignIn
from .forms import ClinicSignUpForm, DistributorSignUpForm
from .models import ClinicSignUp, DistributorSignUp
from django.shortcuts import redirect
from django.contrib.auth import login
from .import views


urlpatterns = [
    path("", views.home, name='supply-home'),
    path('signUp/clinic/', views.clinicsignIn, name='supply-signup-clinic'),
    path('signUp/signIn/', views.SignUp, name='supply-signup-distributor'),
    path('signIn/clinic/', views.signIn, name='supply-signin-clinic'),
    path('signIn/distributor/', views.signIn, name='supply-signin-distributor'),
    path('signUp/', views.SignUp, name='supply-signup'),
    path('signIn/', views.signIn, name='supply-signin'),
    path('signIn/clinicWelcome/', views.clinicWelcome, name='supply-clinic-welcome'),
    path('signIn/distributorWelcome/', views.distributorWelcome, name='supply-distributor-welcome'),
]