from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderItem
from services.models import Service

def view_cart(request):
    """ To render cart details """

    return render (request, 'checkout/cart.html')

def checkout(request):
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)


def add_to_cart(request):
    """ Add a service to the Cart """
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)




