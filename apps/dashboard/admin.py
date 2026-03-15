from django.contrib import admin
from .models import ActivityLog


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):

    list_display = ("action", "created_at")
    search_fields = ("action",)