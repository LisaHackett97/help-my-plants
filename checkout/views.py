from django.shortcuts import render, redirect, reverse, get_object_or_404
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


def add_to_cart(request, item_id):
    """ Add a service to the Cart """
    service = get_object_or_404(Service, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)




