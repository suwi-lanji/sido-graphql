from django.db import models
from apps.products.models import Product
from core.models import Tenant
class Purchase(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=18, decimal_places=2)
    date = models.DateField()