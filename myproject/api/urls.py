from django.urls import path
from .views import ClinicSignUpView, ClinicSignInView


urlpatterns = [
    path('signup/', ClinicSignUpView.as_view(), name='clinic-signUp'),
    path('signin/', ClinicSignInView.as_view(), name='clinic-signIn'),
]