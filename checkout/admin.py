from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'order_total', 'date')

    fields = ('order_number',
              'customer_name',
              'email',
              'phone_number',
              
              'order_total',
              'date'
              )

    list_display = ('order_number', 'customer_name', 'order_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)

