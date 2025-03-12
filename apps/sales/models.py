from django.db import models
from apps.products.models import Product
from core.models import Tenant
class Sale(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=18, decimal_places=2)
    sale_date = models.DateField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"sale_on_{self.sale_date}"