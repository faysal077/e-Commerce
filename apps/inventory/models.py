from django.db import models
from apps.catalog.models import Product


class Inventory(models.Model):

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    stock = models.PositiveIntegerField()

    updated_at = models.DateTimeField(auto_now=True)