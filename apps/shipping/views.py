from django.shortcuts import render


def shipping_list(request):

    return render(request, "shipping/shipping_info.html")