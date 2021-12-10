from django.http import HttpResponse
from .models import Order, OrderItem
from services.models import Service
import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        order_total = round(intent.charges.data[0].amount / 100, 2)
       
        # Clean data in the shipping details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None
        
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                        customer_name__iexact=billing_details.name,
                        email__iexact=billing_details.email,
                        phone_number__iexact=billing_details.phone,
                        order_total=order_total,
                        original_cart=cart,
                        stripe_pid=pid,
                )

                order_exists = True
                break
            
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | Success: Verfied Order already in DB',
                    status=200)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verfied order already in database',
                status=200)   
        

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
