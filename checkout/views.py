from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from services.models import Service
from .forms import OrderForm
from .models import Order, OrderItem
from .contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

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
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {service.name} quantity to {cart[item_id]}')
    else:
            cart[item_id] = quantity
            messages.success(request, f'Added {service.name} to your cart')

    request.session['cart'] = cart        
    return redirect(reverse('view_cart'))

def adjust_cart(request, item_id):
    """
        Adjust the quantity/number of customers
        of the specified service to
        the specified amount
    """
    service = get_object_or_404(Service(), pk=item_id)
    quantity = int(request.POST.get('quantity'))
   
    cart = request.session.get('cart', {})

    if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {service.name} quantity to {cart[item_id]}')
    else:
            cart.pop(item_id)
            messages.success(
                request, f'Removed {service.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('cart'))



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
            
            
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    service = Service.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        service=service,
                        quantity=item_data,
                        )
                    order_line_item.save()
                    
                except Service.DoesNotExist:
                    messages.error(request, (
                        "One of the services in your cart wasn't found in our Database. "
                        "Please call us for assistance")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse('services'))

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
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    """ Handle successful checkouts """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
