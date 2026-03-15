from django.db import models
from apps.orders.models import Order


class ShippingAddress(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    address = models.TextField()

    city = models.CharField(max_length=100)

    postal_code = models.CharField(max_length=20)

    country = models.CharField(max_length=100)