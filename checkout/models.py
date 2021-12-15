""" Models for Order and related Line Items """
import uuid
from django.db.models import Sum
from django.db import models
from django.conf import settings
from services.models import Service
from profiles.models import UserProfile


class Order(models.Model):
    """Order model """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    date = models.DateField(auto_now_add=True)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total for every item added
        """
        self.order_total = self.lineitems.aggregate(
            Sum('item_total'))['item_total__sum'] or 0

        self.total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    """ Related Line Item Model """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    service = models.ForeignKey(Service, null=False, blank=False,
                                on_delete=models.CASCADE)
    date_picked = models.DateField(auto_now_add=False, null=True, blank=True)
    item_total = models.DecimalField(max_digits=6, decimal_places=2,
                                     null=False, blank=False,
                                     editable=False, default=0)

    def save(self, *args, **kwargs):
        self.item_total = self.service.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order total {self.service.price} \
                 for order number {self.order.order_number}'
