from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [

    path('', views.inventory_list, name='inventory_list'),
    # path('add/', views.inventory_add, name='inventory_add'),
    # path('update/<int:id>/', views.inventory_update, name='inventory_update'),
    # path('delete/<int:id>/', views.inventory_delete, name='inventory_delete'),

]