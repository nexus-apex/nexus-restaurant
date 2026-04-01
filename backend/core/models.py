from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[("starters", "Starters"), ("main_course", "Main Course"), ("desserts", "Desserts"), ("beverages", "Beverages"), ("specials", "Specials")], default="starters")
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("available", "Available"), ("unavailable", "Unavailable"), ("seasonal", "Seasonal")], default="available")
    veg = models.BooleanField(default=False)
    spice_level = models.CharField(max_length=50, choices=[("mild", "Mild"), ("medium", "Medium"), ("hot", "Hot")], default="mild")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class TableOrder(models.Model):
    table_number = models.CharField(max_length=255)
    server = models.CharField(max_length=255, blank=True, default="")
    items_count = models.IntegerField(default=0)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("open", "Open"), ("preparing", "Preparing"), ("served", "Served"), ("billed", "Billed"), ("closed", "Closed")], default="open")
    order_time = models.DateField(null=True, blank=True)
    payment = models.CharField(max_length=50, choices=[("cash", "Cash"), ("card", "Card"), ("upi", "UPI")], default="cash")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.table_number

class DiningTable(models.Model):
    table_number = models.CharField(max_length=255)
    capacity = models.IntegerField(default=0)
    section = models.CharField(max_length=50, choices=[("indoor", "Indoor"), ("outdoor", "Outdoor"), ("private", "Private"), ("bar", "Bar")], default="indoor")
    status = models.CharField(max_length=50, choices=[("available", "Available"), ("occupied", "Occupied"), ("reserved", "Reserved")], default="available")
    reserved_name = models.CharField(max_length=255, blank=True, default="")
    reserved_time = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.table_number
