from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from services.models import Service
from .forms import OrderForm
from .models import Order, OrderItem


def view_cart(request):
    """ To render cart details """

    return render(request, 'checkout/cart.html')


def checkout(request):
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)


def add_to_cart(request, item_id):
    """ Add a service to the Cart """
    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] = quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)
