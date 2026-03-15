from django.shortcuts import render
from apps.catalog.models import Product
from .models import Banner


from django.shortcuts import render
from apps.catalog.models import Product, Category


def home(request):

    products = Product.objects.all()[:12]
    categories = Category.objects.all()

    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, "landing/home.html", context)