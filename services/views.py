from django.shortcuts import render, get_object_or_404
from .models import Service
from .forms import ServiceForm

# Create your views here.


def all_services(request):
    """ A view to show all services """

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    """ a view to display individual service details """
    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)


def add_service(request):
    """ Add a service to the site """
    if request.method == 'POST':
        form = ServiceForm(request.Post, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a new service')
            return redirect(reverse('add_service'))
        else:
            messages.error(request, 'Failed to add service. Please check form is valid')
    else:
        form = ServiceForm()
    
    template = 'services/add_service.html'
    context = {
        'form': form
    }

    return render(request, 'services/add_service', context)
