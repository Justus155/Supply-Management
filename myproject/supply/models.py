from email.headerregistry import Group
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser, Permission
class Clinic(models.Model):
    name= models.CharField(max_length=100, unique=True, default='Clinic Name')
    license_number = models.CharField(max_length=15,unique=True, default='C0000000')
    password = models.CharField(max_length=128)
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f"Clinic {self.license_number}"
class Distributor(models.Model):
    subsector = models.CharField(max_length=100, default='Subsector Type', choices=[
            ('Pharmaceutical', 'Pharmaceutical'),
            ('Medical Equipment', 'Medical Equipment'),
            ('Laboratory Supplies', 'Laboratory Supplies'),
            ('Other', 'Other')
        ])
    license_number = models.CharField(max_length=15, unique=True, default='D0000000')
    password = models.CharField(max_length=128)
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)