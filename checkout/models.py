import uuid

from django.db import models
from django.conf import settings
from services.models import Service


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    time_slot = models.DateField(auto_now_add=False, null=True, blank=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateField(auto_now_add=False, null=False, blank=False)

    def _generate_order_number(self):
        """
        Generate a random, unique order number
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    service = models.ForeignKey(Service, null=False, blank=False, on_delete=models.CASCADE)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, 
                                     null=False, blank=False, editable=False, default=0)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order total {self.service.price} for order number {self.order_number}'
