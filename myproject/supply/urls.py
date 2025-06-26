from django.urls import path, include
from . import views

app_name = 'supply'  # This helps with namespacing your URLs

urlpatterns = [
    # home page
    path("", views.home, name="home"),  # Home page
    path("home/", views.home, name="home"),

    #every direct link to clinic signin
    path("signin/", views.clinic_signin, name="clinic_signin"),
    path("clinic_signin/", views.clinic_signin, name="clinic_signin"),
    path("clinic_signin/home/", views.home, name="home"),
    path("clinic_signin/home/clinic_signup/", views.clinic_signup, name="clinic_signup"),
    path("clinic_signin/home/clinic_signup/home/", views.home, name="home"),
    path("clinic_signin/home/clinic_signup/home/clinic_sign_in/", views.home, name="clinic_signin"),
    # Clinic portal
    path("clinic_signin/clinic_portal/", views.clinicPortal, name="clinic_portal"),
    path("clinic_portal/", views.clinicPortal, name="clinic_portal"),
    path("clinic_signin/home/clinic_signup/home/clinic_sign_in/clinic_portal", views.clinic_portal, name="clinic_portal"),
    

    # Clinic signup page
    path("signup/", views.clinic_signup, name="clinic_signup"),
    path("clinic_signup/", views.clinic_signup, name="clinic_signup"),
    path("clinic_signup/home/", views.home, name="home"),
    path("clinic_signup/home/clinic_signup/", views.clinic_signup, name="clinic_signup"),
    path("clinic_signup/home/clinic_signin/home/", views.home, name="home"),
    path("clinic_signup/home/clinic_signin/home/clinic_signin/", views.clinic_signin, name="clinic_signin"),
    path("clinic_signup/home/clinic_signin/home/clinic_signin/clinic_portal", views.clinic_portal, name="clinic_portal"),
    path("clinic_signup/home", views.clinic_signup_home, name="home2"),
    #distributor signup page
    path("distributor_signup/", views.distributor_signup, name="distributor_signup"),
    path("distributor_signup/home/", views.home, name="home"),
    path("distributor_signup/home/distributor_signup/", views.distributor_signup, name="distributor_signup"),
    path("distributor_signup/home/distributor_signin/", views.distributor_signin, name="distributor_signin"),
    path("distributor_signup/home/distributor_signin/distributor_portal", views.distributor_portal, name="distributor_portal"),
    #distributor signup page   
    path("distributor_signin/", views.distributor_signin, name="distributor_signin"),
    path("distributor_signin/home/", views.home, name="home"),
    path("distributor_signin/home/distributor_signup/", views.distributor_signup, name="distributor_signup"),
    path("distributor_signin/home/distributor_signin/", views.distributor_signin, name="distributor_signin"),
    path("distributor_signin/home/distributor_signin/distributor_portal", views.distributor_portal, name="distributor_portal"), 

]