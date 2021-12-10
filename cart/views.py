from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def view_cart(request):
    """ To render cart details """

    return render(request, 'cart/cart.html')
