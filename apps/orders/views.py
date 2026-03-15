from django.shortcuts import render, redirect
from .models import Order
from apps.cart.models import Cart, CartItem


def checkout(request):

    cart = Cart.objects.filter(user=request.user).first()

    items = CartItem.objects.filter(cart=cart)

    return render(request, "orders/checkout.html", {"items": items})


def place_order(request):

    cart = Cart.objects.filter(user=request.user).first()

    items = CartItem.objects.filter(cart=cart)

    total = sum(i.product.price * i.quantity for i in items)

    order = Order.objects.create(
        user=request.user,
        total_price=total
    )

    for item in items:
        order.orderitem_set.create(
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    items.delete()

    return redirect("orders:order_success")


def order_success(request):

    return render(request, "orders/order_success.html")