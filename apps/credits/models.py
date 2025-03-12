from django.db import models
from core.models import Tenant
class Credit(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    debtor = models.CharField(max_length=100, db_index=True)
    status = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    pending_balance = models.DecimalField(max_digits=18, decimal_places=2)
    credit_date = models.DateField()
    returned_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)