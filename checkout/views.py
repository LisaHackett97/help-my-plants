from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from services.models import Service
from .forms import OrderForm
from .models import Order, OrderItem


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

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JslSmGgXmJ73lYIjBGsO8ylNfJOFQLZBnb9PpxuXExjXkNxiPByQZEvCsHUYxiXPgOpABZ1SBgoYwikNmn8VdKe00UaIgTZ95',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)


@login_required
def checkout_success(request):
    """ Render Success Page """
    return render(request, 'checkout/checkout_success.html')
