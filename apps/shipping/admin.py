from django.contrib import admin
from .models import ShippingAddress


@admin.register(ShippingAddress)
class ShippingAdmin(admin.ModelAdmin):

    list_display = ("order", "city", "postal_code", "country")
    search_fields = ("city", "country")