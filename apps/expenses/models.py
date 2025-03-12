from django.db import models
from core.models import Tenant
class Expense(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    category = models.CharField(max_length=100, db_index=True)
    expense_date = models.DateField()