from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    safety_quauntity = models.IntegerField(default=1)
    quantity_in_stock = models.IntegerField(default=0)

    def __str__(self):
        return f"product_{self.name}_k{self.price}"