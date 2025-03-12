from django.db import models
from apps.products.models import Product
class InventoryAdjustment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    adjustment_type = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=18, decimal_places=2)