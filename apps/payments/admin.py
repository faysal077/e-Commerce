from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = ("order", "method", "amount", "transaction_id", "status", "created_at")
    search_fields = ("transaction_id",)
    list_filter = ("method", "status")