from django.shortcuts import render
from apps.catalog.models import Product, Category
from .models import Banner


def home(request):

    banners = Banner.objects.filter(active=True)

    categories = Category.objects.all()

    featured_products = Product.objects.filter(
        is_active=True,
        is_featured=True
    )[:8]

    best_sellers = Product.objects.filter(
        is_active=True,
        is_best_seller=True
    )[:8]

    trending_products = Product.objects.filter(
        is_active=True,
        is_trending=True
    )[:8]

    context = {
        "banners": banners,
        "categories": categories,
        "featured_products": featured_products,
        "best_sellers": best_sellers,
        "trending_products": trending_products,
    }

    return render(request, "landing/home.html", context)