from django.urls import path
from . import views

app_name = "shipping"

urlpatterns = [

    path('', views.shipping_list, name='shipping_list'),
    # path('add/', views.shipping_create, name='shipping_create'),
    # path('update/<int:id>/', views.shipping_update, name='shipping_update'),
    # path('delete/<int:id>/', views.shipping_delete, name='shipping_delete'),

]