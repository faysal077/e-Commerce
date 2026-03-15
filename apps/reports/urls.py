from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [

    path('', views.report_dashboard, name='report_dashboard'),
    # path('sales/', views.sales_report, name='sales_report'),
    # path('inventory/', views.inventory_report, name='inventory_report'),
    # path('orders/', views.order_report, name='order_report'),

]