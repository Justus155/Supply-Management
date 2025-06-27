from django import forms
from .models import Clinic, Distributor

class loginForm(forms.Form):
    clinic_license = forms.CharField(max_length=15, required=False, label='Clinic License')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    distributor_license = forms.CharField(max_length=15, required=False, label='Distributor License')
    def clean(self):
        cleaned_data = super().clean()
        clinic_license = cleaned_data.get("clinic_license")
        distributor_license = cleaned_data.get("distributor_license")

        if not clinic_license and not distributor_license:
            raise forms.ValidationError("Please enter either a Clinic or Distributor license.")

        if clinic_license and not clinic_license.startswith('C'):
            raise forms.ValidationError("Clinic license must start with 'C'.")

        if distributor_license and not distributor_license.startswith('D'):
            raise forms.ValidationError("Distributor license must start with 'D'.")
        
        return cleaned_data
class signupForm(forms.Form):
    class Meta:
        model = Clinic
        fields = ['name','license_number', 'password']
    name = forms.CharField(max_length=100, required=True, label='Clinic Name')
    license_number = forms.CharField(max_length=15, required=True, label='Clinic License Number')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        model = Distributor
        fields = ['subsector','license_number', 'password']
    subsector = forms.ChoiceField(
        choices=[
            ('Pharmaceutical', 'Pharmaceutical'),
            ('Medical Equipment', 'Medical Equipment'),
            ('Laboratory Supplies', 'Laboratory Supplies'),
            ('Other', 'Other')
        ],
        required=True,
        label='Subsector Type'
    )
    license_number = forms.CharField(max_length=15, required=True, label='Distributor License Number')
    # Assuming distributor_license is a field in Distributor model    
    password = forms.CharField(widget=forms.PasswordInput, label='Password')





    def clean_license_number(self):
        license_number = self.cleaned_data.get('license_number')
        if not (license_number.startswith('C') or license_number.startswith('D')):
            raise forms.ValidationError("License must start with 'C' (Clinic) or 'D' (Distributor).")
        return license_number

