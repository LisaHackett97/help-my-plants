from datetime import datetime
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    time_slot = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name
