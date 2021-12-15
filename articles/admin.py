""" Admin and register app """
from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    """ Dispay of model in Admin """
    list_display = (
        'title',
        'content',
        'image',
        'created_date',
        )


admin.site.register(Article, ArticleAdmin)
