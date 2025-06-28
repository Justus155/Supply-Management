from django.contrib import admin
from .models import clinic, accounts_clinic_up

# Register your models here.
admin.site.register(clinic)
admin.site.register(accounts_clinic_up)  # Register the clinic_up model if needed
