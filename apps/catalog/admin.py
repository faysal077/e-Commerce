from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ("name", "category", "price", "is_active", "is_featured", "is_best_seller", "is_trending", "created_at")
    list_filter = ("category", "is_active", "is_featured", "is_best_seller", "is_trending")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}