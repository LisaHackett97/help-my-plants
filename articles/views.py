from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article
from services.models import Service


@login_required()
def all_articles(request):
    """ A view to show all articles """

    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/articles.html', context)

# These are views so that when the user clocks on the links, will bring them straitgh to the service detail page
# Need to look at refactoring code. Filter etc
# These are 3 products linked to on the articles page
@login_required()
def get_serviceOne(request):
    service = Service.objects.get(id="1")
    context = {
        'service': service,
    }
    return render(request, 'services/service_detail.html', context)


@login_required()
def get_serviceTwo(request):
    service = Service.objects.get(id="2")
    context = {
        'service': service,
    }
    return render(request, 'services/service_detail.html', context)


@login_required()
def get_serviceThree(request):
    service = Service.objects.get(id="3")
    context = {
        'service': service,
    }
    return render(request, 'services/service_detail.html', context)
