from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer_name', 'email', 'phone_number',
                  'time_slot', 'order_total',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders 
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'customer_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'time_slot': 'Time Chosen',
            }

       
       
