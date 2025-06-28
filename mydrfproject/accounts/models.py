from django.db import models
from django.contrib.auth.models import AbstractUser

class clinic(AbstractUser):
    license_number = models.CharField(max_length=15, unique=True, default='C0')
    name= models.CharField(max_length=100, unique=True, default='Clinic Name')
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return f"clinic {self.license_number}"
# Create your models here.
class accounts_clinic_up(models.Model):
    name = models.CharField(max_length=100, unique=True, default='Clinic Name')
    license = models.CharField(max_length=15, unique=True, default='C0')
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"clinic {self.license}"
    
    class Meta:
        verbose_name_plural = "clinics"
class InventoryItem(models.Model):
    clinic = models.ForeignKey(clinic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    expiry_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Sufficient', 'Sufficient'), ('Low', 'Low'), ('Critical', 'Critical')])
    
class Order(models.Model):
    clinic = models.ForeignKey(clinic, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=10, unique=True)
    items = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Completed', 'Completed')])
    priority = models.CharField(max_length=20, choices=[('Routine', 'Routine'), ('Refill', 'Refill'), ('Urgent', 'Urgent')])
    date_placed = models.DateField(auto_now_add=True)

class Service(models.Model):
    clinic = models.ForeignKey(clinic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()