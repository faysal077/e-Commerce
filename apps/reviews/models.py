from django.db import models
from apps.catalog.models import Product
from apps.accounts.models import User


class Review(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)