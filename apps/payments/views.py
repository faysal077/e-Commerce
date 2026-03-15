from django.shortcuts import render


def payment_page(request):

    return render(request, "payments/payment_page.html")


def payment_success(request):

    return render(request, "payments/payment_success.html")


def payment_failed(request):

    return render(request, "payments/payment_failed.html")