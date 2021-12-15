""" Views for Bopkings app """
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order
from profiles.models import UserProfile
from .forms import BookingForm


def bookings_list(request):
    """ A view to return the index page """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.all()

    context = {
        'profile': profile,
        'orders': orders,
        }

    return render(request, 'bookings/bookings_list.html', context)


@login_required
def update_order(request, order_id):
    """ Edit a order to update Booking Date for Order """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    order = get_object_or_404(Order, pk=order_id)
    form = BookingForm(instance=order)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=order)
        if form.is_valid():
            # Post functionality to update the date field
            # on each line item in the customers order has not been finalised
            # Giving the authenticated user a message
            messages.error(request,
                           'Please contact your admin. We are currently experiencing \
                            issues with this functionality. \
                            The order has not been Updated')
            return redirect(reverse('bookings_list'))
    else:
        form = BookingForm(instance=order)
        messages.info(request, f'Apologies. \
            Order for { order.customer_name } cannot be updated at this time')

    template = 'bookings/update_order.html'

    context = {
        'form': form,
        'order': order,
    }

    return render(request, template, context)
