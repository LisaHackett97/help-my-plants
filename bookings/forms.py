""" to render a form to update a line item on an order """
from django import forms
from checkout.models import OrderItem


class BookingForm(forms.ModelForm):
    """ BookingForm to display the lineItem date picked field
    and allow admin to update
    Functionality not fully in place yet
    """
    class Meta:
        model = OrderItem
        fields = ('date_picked',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
