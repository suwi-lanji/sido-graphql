from django.db import models
from django.contrib.auth.models import AbstractUser

class Tenant(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=255)
    logo_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
class User(AbstractUser):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)