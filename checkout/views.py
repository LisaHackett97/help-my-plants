from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from services.models import Service
from .forms import OrderForm
from .models import Order, OrderItem


def view_cart(request):
    """ To render cart details """

    return render(request, 'checkout/cart.html')


def add_to_cart(request, item_id):
    """ 
    Add a service to the Cart 
    User can only add one item for each service to cart
    They are redirected to cart
    """
    service = Service.objects.get(pk=item_id)   
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id)
    request.session['cart'] = cart
    messages.success(request, f'Added {service.name} to your order')
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove an item from the cart """
    cart = request.session.get('cart', {})
    service = Service.objects.get(pk=item_id) 
    cart.pop(item_id)
    request.session['cart'] = cart
    messages.success(
                request, f'Removed {service.name} from your cart')
    return redirect(reverse('view_cart'))



def checkout(request):
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)