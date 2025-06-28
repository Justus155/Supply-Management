from django import forms
from .models import clinic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class signupForm(UserCreationForm):
    name= forms.CharField(max_length=100, required=True, label='Clinic Name')
    license_number = forms.CharField(max_length=15, required=True, label='Clinic License Number')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        model = clinic
        fields = ['name', 'license_number', 'password1']
        help_texts = {
            'name': 'Enter the name of the clinic.',
            'license_number': 'Enter a unique license number for the clinic.',
            'password1': 'Enter a secure password for the clinic account.'
        }

class loginForm(AuthenticationForm):
    class Meta:
        model = clinic
        fields = ['license_number', 'password'] # Assuming 'password' is a field in Clinic model
    license_number = forms.CharField(max_length=5, required=True, label='Clinic License Number')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
