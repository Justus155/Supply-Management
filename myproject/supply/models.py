from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

#creating an adbstract class for common fields
class Clinic (AbstractUser):

    clinic_license = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['clinic_license', 'password']
    def __str__(self):
        return self.clinic_license
class distributor(models.Model):
    distributor_license = models.CharField(max_length=100, unique=True)
    name= models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['distributor_license', 'password']

    @property
    def is_anonymous(self):
        return False  # Or implement custom logic

    @property
    def is_authenticated(self):
        return True   # Or implement custom logic
    
    def __str__(self):
        return self.distributor_license

