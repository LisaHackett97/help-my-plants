from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Service
from .forms import ServiceForm

# Create your views here.

@login_required
def all_services(request):
    """ A view to show all services """

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)

@login_required
def service_detail(request, service_id):
    """ a view to display individual service details """
    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)

@login_required
def add_service(request):
    """ Add a service to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))
        
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Successfully added service!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Failed to add service. Please ensure the form is valid.')
    else:
        form = ServiceForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_service(request, service_id):
    """ Edit a service in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Failed to update service. Please ensure the form is valid.')
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'services/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)

@login_required
def delete_service(request, service_id):
    """ Delete a service from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Service deleted!')
    return redirect(reverse('services'))