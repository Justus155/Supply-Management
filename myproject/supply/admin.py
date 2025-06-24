from django.contrib import admin
from  .models import ClinicSignUp, DistributorSignUp
from .forms import ClinicSignUpForm, DistributorSignUpForm
from django.contrib.auth import login
from .models import Product, Supplier, Order

# Register your models here.
admin.site.register(ClinicSignUp)
admin.site.register(DistributorSignUp)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Order)
