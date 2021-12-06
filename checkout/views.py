from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from services.models import Service
from .forms import OrderForm
from .models import Order, OrderItem
from .contexts import cart_contents

import stripe

@login_required
def view_cart(request):
    """ To render cart details """

    return render(request, 'checkout/cart.html')


@login_required
def add_to_cart(request, item_id):
    """
    Add a service to the Cart
    User can only add one item for each service to cart
    They are redirected to cart
    """
    service = get_object_or_404(Service, pk=item_id)
    cart = request.session.get('cart', {})

    if item_id in cart:
        messages.info(request, f'{service.name} already in your cart')
    else:
        cart[item_id] = cart.get(item_id)
        request.session['cart'] = cart
        messages.success(request, f'Added {service.name} to your order')
    return redirect(reverse('view_cart'))


@login_required
def remove_from_cart(request, item_id):
    """ Remove an item from the cart """
    cart = request.session.get('cart', {})
    service = get_object_or_404(Service, pk=item_id)
    cart.pop(item_id)
    request.session['cart'] = cart
    messages.success(
                request, f'Removed {service.name} from your cart')
    return redirect(reverse('view_cart'))


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get('cart', {})
        form_data = {
            'customer_name': request.POST['customer_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'time_slot': request.POST['time_slot'],
            'order_total': request.POST['order_total'],
        }
        order_form = OrderForm(form_data)
    else:
        order_form = OrderForm()

    current_cart = cart_contents(request)
    total = current_cart['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe Public key is missing. Did you forget to set it on your environment?')
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'stripe_public_key',
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request):
    """ Render Success Page """
    return render(request, 'checkout/checkout_success.html')
