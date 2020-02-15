from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import generic

from .models import Article


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')

class ArticleView(generic.DetailView):
    template_name = 'article.html'
    context_object_name = 'article'
    model = Article
