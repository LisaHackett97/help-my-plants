""" Imports and Views to render data on Articles app"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from services.models import Service
from profiles.models import UserProfile
from .models import Article


@login_required()
def all_articles(request):
    """ A view to show all articles """
    profile = get_object_or_404(UserProfile, user=request.user)
    articles = Article.objects.all()
    orders = profile.orders.all()
    context = {
        'articles': articles,
        'orders': orders,
    }
    return render(request, 'articles/articles.html', context)


# These are views so that when the user clicks on the links,
# They will be brought straight to the service detail page
# Code needs to be refactored but due to time contraints this hasn't been done
# These are 3 products linked to on the articles page
@login_required()
def getServiceOne(request):
    """ to access service 1"""
    service = Service.objects.get(id="1")
    context = {
        'service': service,
    }
    return render(request, 'services/service_detail.html', context)


@login_required()
def getServiceTwo(request):
    """ to access service by its id"""
    service = Service.objects.get(id="2")
    context = {
        'service': service,
    }
    return render(request, 'services/service_detail.html', context)


@login_required()
def getServiceThree(request):
    """ to access service by its id"""
    service = Service.objects.get(id="3")
    context = {
        'service': service,
    }
    return render(request, 'services/service_detail.html', context)
