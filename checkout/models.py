import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from services.models import Service


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    service = models.ForeignKey(Service, null=False, blank=False, on_delete=models.CASCADE)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
