from django.urls import path
from . import views

app_name = "accounts_finance"

urlpatterns = [

    path('', views.finance_dashboard, name='finance_dashboard'),
    # path('transactions/', views.transaction_list, name='transaction_list'),
    # path('transactions/add/', views.transaction_create, name='transaction_create'),

]