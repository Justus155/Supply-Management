from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password, check_password

class Clinic(models.Model):
    license_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex='^C[A-Z0-9]{4,14}$',
                message='Clinic license must start with C followed by 4-14 alphanumeric characters',
                code='invalid_clinic_license'
            )
        ]
    )
    password = models.CharField(max_length=128)  # Store hashed passwords
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f"Clinic {self.license_number}"

class Distributor(models.Model):
    license_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex='^D[A-Z0-9]{4,14}$',
                message='Distributor license must start with D followed by 4-14 alphanumeric characters',
                code='invalid_distributor_license'
            )
        ]
    )
    password = models.CharField(max_length=128)  # Store hashed passwords
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f"Distributor {self.license_number}"