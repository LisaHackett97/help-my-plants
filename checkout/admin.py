from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'order_total', 'date',
                       'original_bag',
                       'stripe_pid')

    fields = ('order_number',
              'customer_name',
              'email',
              'phone_number',
              'time_slot',
              'order_total',
              'date',
              'original_bag', 
              'stripe_pid')

    list_display = ('order_number', 'customer_name', 'time_slot', 'order_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)

