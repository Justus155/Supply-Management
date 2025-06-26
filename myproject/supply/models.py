from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
class Clinic(models.Model):
    name= models.CharField(max_length=100)
    license_number = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=128)

class Distributor(AbstractUser):
    SUBSECTOR_CHOICES = [
        ('WHOLESALE', 'Wholesale Distributor'),
        ('SPECIALTY', 'Specialty Medicine Distributor'),
        ('GOVERNMENT', 'Government Medical Store'),
    ]
    
    subsector_type = models.CharField(max_length=20, choices=SUBSECTOR_CHOICES)
    license_number = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128, verbose_name='password')
    
    def __str__(self):
        return f"{self.username} ({self.get_subsector_type_display()})"



    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f"Clinic {self.license_number}"
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f"Distributor {self.license_number}"
    
from django.contrib.auth.models import AbstractUser
