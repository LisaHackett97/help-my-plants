
from django.urls import path
from .import views

urlpatterns = [
    path('', views.bookings_list, name='bookings_list'),
    path('update/<int:order_id>', views.update_order, name='update_order'),
]
