from django.shortcuts import render
from .models import Coupon


def coupon_list(request):

    coupons = Coupon.objects.filter(active=True)

    return render(request, "coupons/coupon_list.html", {"coupons": coupons})