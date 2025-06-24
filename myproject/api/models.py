from django.db import models
class clinic(models.Model):
    clinic_license = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
class distributor(models.Model):
    distributor_license = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)