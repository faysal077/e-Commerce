from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):

    products = Product.objects.filter(is_active=True)

    return render(request, "catalog/product_list.html", {"products": products})


def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)

    return render(request, "catalog/product_detail.html", {"product": product})


def category_products(request, slug):

    category = get_object_or_404(Category, slug=slug)

    products = Product.objects.filter(category=category)

    return render(request, "catalog/category_products.html", {
        "category": category,
        "products": products
    })