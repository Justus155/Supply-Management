from .models import Clinic, Distributor
from django.contrib import admin


admin.site.register(Clinic)
admin.site.site_header = "Supply Management Admin"
admin.site.register(Distributor)

# Register your models here.





