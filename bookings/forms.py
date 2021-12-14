from django import forms

from checkout.models import Order
from checkout.models import OrderItem


class BookingForm(forms.ModelForm):
    class Meta:
        
        model = OrderItem
        fields = ( 'date_picked',
                  )   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'date_picked': 'Date confirmed with customer',           
        }
       
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-content'

        
