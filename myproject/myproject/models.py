from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class User(AbstractUser):
    ROLES = (
        ('CLINIC', 'Clinic/Pharmacy'),
        ('DRIVER', 'Delivery Driver'),
        ('DISTRIBUTOR', 'Distribution Organization'),
        ('ADMIN', 'System Admin'),
    )
    role = models.CharField(max_length=12, choices=ROLES)
    phone = models.CharField(max_length=15, unique=True)
    county = models.CharField(max_length=50)
    is_approved = models.BooleanField(default=False)  # For admin approval of distributors

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class Clinic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'CLINIC'})
    license_number = models.CharField(max_length=50, unique=True)
    facility_level = models.CharField(max_length=1, choices=[('1', 'Level 1'), ('4', 'Level 4')])  # From Ch.2
    gps_lat = models.DecimalField(max_digits=9, decimal_places=6)
    gps_lon = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.user.username} (Level {self.facility_level})"

class Distributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'DISTRIBUTOR'})
    organization_name = models.CharField(max_length=100)
    warehouse_location = models.CharField(max_length=100)

    def __str__(self):
        return self.organization_name

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)  # National drug code
    requires_cold_chain = models.BooleanField(default=False)
    minimum_stock = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Inventory(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    current_stock = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('clinic', 'medicine')

    def is_below_threshold(self):
        return self.current_stock < self.medicine.minimum_stock

    def __str__(self):
        return f"{self.medicine} at {self.clinic}: {self.current_stock} units"

class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending Approval'),
        ('APPROVED', 'Approved by Distributor'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    )
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_items(self):
        return self.orderitem_set.count()

    def __str__(self):
        return f"Order #{self.id} - {self.clinic} → {self.distributor}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.quantity}x {self.medicine} for Order #{self.order.id}"

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'DRIVER'})
    tracking_code = models.CharField(max_length=20, unique=True)
    current_location = models.CharField(max_length=100, blank=True)
    estimated_delivery = models.DateTimeField(null=True, blank=True)
    actual_delivery = models.DateTimeField(null=True, blank=True)

    def update_location(self, lat, lon):
        self.current_location = f"{lat},{lon}"
        self.save()

    def __str__(self):
        return f"Delivery #{self.tracking_code} for Order #{self.order.id}"

class TemperatureLog(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.temperature}°C at {self.timestamp}"