from django.urls import path
from . import views

app_name = "coupons"

urlpatterns = [

    path('', views.coupon_list, name='coupon_list'),
#     path('create/', views.coupon_create, name='coupon_create'),
#     path('update/<int:id>/', views.coupon_update, name='coupon_update'),
#     path('delete/<int:id>/', views.coupon_delete, name='coupon_delete'),

]