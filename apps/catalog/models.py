from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to="products/", blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    @property
    def image_or_placeholder(self):
        if self.image:
            return self.image.url
        return f"https://picsum.photos/seed/{self.slug}/300/400"  
