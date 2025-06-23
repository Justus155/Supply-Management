from django import forms

from .models import ClinicSignUp, DistributorSignUp

class ClinicSignUpForm(forms.ModelForm):
    class Meta:
        model = ClinicSignUp
        fields = [ 'clinic_license', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
class DistributorSignUpForm(forms.ModelForm):
    class Meta:
        model = DistributorSignUp
        fields = ['distributor_license', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }