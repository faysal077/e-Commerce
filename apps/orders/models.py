from django.db import models
from apps.accounts.models import User
from apps.catalog.models import Product


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=50,
        default="pending"
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)