from django.db import models
from django.contrib.auth.models import AbstractUser

class clinic(AbstractUser):
    license_number = models.CharField(max_length=15, unique=True, default='C0')
    name= models.CharField(max_length=100, unique=True, default='Clinic Name')
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return f"clinic {self.license_number}"
# Create your models here.
