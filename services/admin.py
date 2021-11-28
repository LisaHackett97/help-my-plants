from django.contrib import admin
from .models import Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'time_slot',
        'price',
        'image',
    )

admin.site.register(Service, ServiceAdmin)
