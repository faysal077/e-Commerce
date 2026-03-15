from django.shortcuts import render, redirect
from .models import Cart, CartItem
from apps.catalog.models import Product


def cart_detail(request):

    cart = Cart.objects.filter(user=request.user).first()

    items = CartItem.objects.filter(cart=cart) if cart else []

    return render(request, "cart/cart_detail.html", {"items": items})


def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        item.quantity += 1
        item.save()

    return redirect("cart:cart_detail")


def remove_from_cart(request, product_id):

    cart = Cart.objects.filter(user=request.user).first()

    if cart:
        CartItem.objects.filter(cart=cart, product_id=product_id).delete()

    return redirect("cart:cart_detail")