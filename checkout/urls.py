from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('add/<item_id>', views.add_to_cart, name='add_to_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('wh/', webhook, name='webhook'),
]
