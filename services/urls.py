from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.all_services, name='services'),
    path('<service_id>', views.service_detail, name='service_detail'),
]