from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [

    path('', views.notification_list, name='notification_list'),
    # path('mark-read/<int:id>/', views.mark_as_read, name='mark_as_read'),
    # path('delete/<int:id>/', views.notification_delete, name='notification_delete'),

]