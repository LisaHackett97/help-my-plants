from django.shortcuts import render
from .models import Service


# Create your views here.

def all_services(request):
    """ A view to show all services """

    services = Service.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'services/services.html', context)

