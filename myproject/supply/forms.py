from email import header
from django import forms

from .models import ClinicSignUp, DistributorSignUp
from .models import clinicSignIn, DistributorSignIn

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
class ClinicLoginForm():
    clinic_license = forms.CharField(label="license")
    password = forms.CharField(widget=forms.PasswordInput)
    def confirm_login(self, user):
        try:
            clinic = clinicSignIn.objects.get(clinic_license=self.cleaned_data['clinic_license'])
            if clinic.password == self.cleaned_data['password']:
                return  True
            else:
                return False
        except clinicSignIn.DoesNotExist:
            return False
class DistributorLoginForm():
    distributor_license = forms.CharField(label="license")
    password = forms.CharField(widget=forms.PasswordInput)
    def confirm_login(self, user):
        try:
            distributor = DistributorSignIn.objects.get(distributor_license=self.cleaned_data['distributor_license'])
            if distributor.password == self.cleaned_data['password']:
                return True
            else:
                return False
        except DistributorSignIn.DoesNotExist:
            return False