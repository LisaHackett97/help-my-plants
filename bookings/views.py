from django.shortcuts import render, get_object_or_404
from checkout.models import Order
from profiles.models import UserProfile

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
