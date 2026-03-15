from django.db import models
from apps.accounts.models import User


class Transaction(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    type = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)