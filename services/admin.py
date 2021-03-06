""" Admin for the Services Model """
from django.contrib import admin
from .models import Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'image',
    )


admin.site.register(Service, ServiceAdmin)
