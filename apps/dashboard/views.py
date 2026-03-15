from django.shortcuts import render
from apps.orders.models import Order
from apps.accounts.models import User


def dashboard_home(request):

    total_orders = Order.objects.count()

    total_users = User.objects.count()

    return render(request, "dashboard/home.html", {
        "total_orders": total_orders,
        "total_users": total_users
    })