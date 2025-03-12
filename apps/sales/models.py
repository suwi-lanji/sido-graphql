from django.db import models
from apps.products.models import Product
class Sale(models.Model):
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=18, decimal_places=2)
    sale_date = models.DateField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"sale_on_{self.sale_date}"