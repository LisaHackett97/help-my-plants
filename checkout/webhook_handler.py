from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe Webhooks"""
    
    """ a setup method thats called every time an instance of the class is created """
    def __init__(self, request):
        self.request - request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
