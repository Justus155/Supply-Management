from django.urls import path
from . import views

app_name = 'supply'  # This helps with namespacing your URLs

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # Clinic authentication URLs
    path('signup/', views.clinic_signup, name='clinic_signup'),
    path('clinic/signin/', views.clinic_signin, name='clinic_signin'),
    path('clinic/portal/', views.clinic_portal, name='clinic_portal'),
    
    # Distributor authentication URLs
    path('distributor/signup/', views.distributor_signup, name='distributor_signup'),
    path('distributor/signin/', views.distributor_signin, name='distributor_signin'),
    path('distributor/portal/', views.distributor_portal, name='distributor_portal'),
]