from django.conf import settings
from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe webhook
    """

    def __init__(self, request):
        self.request = rerquest

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
