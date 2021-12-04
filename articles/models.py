from django.db import models
from django.conf import settings
from services.models import Service


class Article(models.Model):
    title = models.CharField(max_length=264, null=False, blank=False)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=False, null=False, blank=False)

    def __str__(self):
        return self.title

