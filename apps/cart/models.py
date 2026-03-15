from django.db import models
from apps.accounts.models import User
from apps.catalog.models import Product


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.product)