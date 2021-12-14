from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from checkout.models import Order
from profiles.models import UserProfile
from checkout.forms import OrderForm
from django.contrib.auth.decorators import login_required
from .forms import BookingForm

# Create your views here.

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
            form.save()
            messages.success(request, 'Successfully updated booking!')
            
        else:
            messages.error(request, 'Failed to update service. Please ensure the form is valid.')
    else:
        form = BookingForm(instance=order)
        
        messages.info(request, f'You are editing { order.customer_name }')

    template = 'bookings/update_order.html'
    
    context = {
        'form': form,
        'order': order,
    }

    return render(request, 'bookings/update_order.html', context)
