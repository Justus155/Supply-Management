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
    #home url
    path("", views.home, name='supply-home'),
    #SIGN IN TO SIGNUP
    path('signIn/signUp/',views.SignUp, name='clinic_sign-up'),

    #clinic sign-up and in
    path('signIn/clinic/', views.clinic_sign_in, name='clinic_sign_in'),
    path('signup/clinic/', views.clinic_sign_up, name='clinic_sign_up'),
    path('clinic_welcome/', views.clinic_welcome, name='clinic_welcome'),
    path('signUp/clinic/', views.clinicsignIn, name='supply-signup-clinic'),
    path('signUp/signIn/', views.SignUp, name='supply-signup-distributor'),
    path('signIn/clinic/', views.signIn, name='supply-signin-clinic'),


    #distributor signIn and Up

    path('distributor/sign-in/', views.distributor_sign_in, name='distributor_sign_in'),
    path('distributor/sign-up/', views.distributor_sign_up, name='distributor_sign_up'),
    path('distributor/welcome/', views.distributor_welcome, name='distributor_welcome'),
    path('signIn/distributor/', views.signIn, name='supply-signin-distributor'),


    #signup and signin urls

    path('signUp/', views.SignUp, name='supply-signup'),
    path('signIn/', views.signIn, name='supply-signin'),
    path('signIn/clinicWelcome/', views.clinic_welcome, name='supply-clinic-welcome'),
    path('signIn/distributorWelcome/', views.distributor_welcome, name='supply-distributor-welcome'),
]
