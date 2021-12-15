""" Articles Model """
from django.db import models
from django.conf import settings


class Article(models.Model):
    """ Fields that can be viewed to article page"""
    title = models.CharField(max_length=264, null=False, blank=False)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=False,
                                    null=False,
                                    blank=False)

    def __str__(self):
        return self.title
