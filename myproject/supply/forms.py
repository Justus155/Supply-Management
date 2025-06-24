from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import  DistributorSignIn, clinicSignIn  # Using the improved models from earlier

# CLINIC FORMS
class ClinicSignUpForm(UserCreationForm):
    clinic_license = forms.CharField(
        max_length=100,
        help_text='Required. Your official clinic license number.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = clinicSignIn
        fields = ('clinic_license', 'password1')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['clinic_license']  # Using license as username
        if commit:
            user.save()
        return user

class ClinicSignInForm(AuthenticationForm):
    clinic_license = forms.CharField(
        label="Clinic License",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')  # We use clinic_license instead
    
    def clean(self):
        clinic_license = self.cleaned_data.get('clinic_license')
        password = self.cleaned_data.get('password')
        
        if clinic_license and password:
            self.user_cache = authenticate(
                self.request,
                clinic_license=clinic_license,
                password=password
            )
            if self.user_cache is None:
                raise ValidationError("Invalid clinic license or password")
            elif not self.user_cache.is_active:
                raise ValidationError("This clinic account is inactive")
        
        return self.cleaned_data

# DISTRIBUTOR FORMS
class DistributorSignUpForm(UserCreationForm):
    distributor_license = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    subsection = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = DistributorSignIn
        fields = ('distributor_license', 'subsection', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['distributor_license']
        if commit:
            user.save()
        return user

class DistributorSignInForm(AuthenticationForm):
    distributor_license = forms.CharField(
        label="Distributor License",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')  # We use distributor_license instead
    
    def clean(self):
        distributor_license = self.cleaned_data.get('distributor_license')
        password = self.cleaned_data.get('password')
        
        if distributor_license and password:
            self.user_cache = authenticate(
                self.request,
                distributor_license=distributor_license,
                password=password
            )
            if self.user_cache is None:
                raise ValidationError("Invalid distributor license or password")
            elif not self.user_cache.is_active:
                raise ValidationError("This distributor account is inactive")
            elif not hasattr(self.user_cache, 'is_distributor'):
                raise ValidationError("Not a distributor account")
        
        return self.cleaned_data