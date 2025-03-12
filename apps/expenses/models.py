from django.db import models

class Expense(models.Model):
    description = models.TextField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    category = models.CharField(max_length=100, db_index=True)
    expense_date = models.DateField()