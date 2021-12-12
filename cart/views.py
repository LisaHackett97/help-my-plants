from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from services.models import Service

@login_required
def view_cart(request):
    """ To render cart details """

    return render(request, 'cart/cart.html')

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
    cart= request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {service.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {service.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


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
