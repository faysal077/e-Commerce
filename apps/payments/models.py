from django.db import models
from apps.orders.models import Order


class Payment(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    method = models.CharField(max_length=50)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    transaction_id = models.CharField(max_length=255)

    status = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)