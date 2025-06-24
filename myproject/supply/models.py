from django.db import models


# Create your models here.
class clinicSignIn(models.Model):
    clinic_license = models.CharField(max_length=100, default='permanent_license',unique=True)
    password = models.CharField(max_length=128)
class DistributorSignIn(models.Model):    
    distributor_license = models.CharField(max_length=100, default='permanent_license',unique=True)
    password = models.CharField(max_length=128)
class ClinicSignUp(models.Model):
    clinic_license = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
class DistributorSignUp(models.Model):
    distributor_license = models.CharField(max_length=100, unique=True)
    subsection = models.CharField(max_length=100)
    password = models.CharField(max_length=128)        
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('normal', 'Pending'),
        ('EMERGENCY', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ], default='PENDING')
    def __str__(self):
        return self.name