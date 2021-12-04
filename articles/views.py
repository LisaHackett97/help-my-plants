from django.shortcuts import render
from django.contrib import messages

from .models import Article


def all_articles(request):
    """ A view to show all articles """

    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/articles.html', context)
