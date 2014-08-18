from django.shortcuts import render_to_response

from article.models import Article
from category.models import Category


def list_categories(request, **kwargs):
    context = kwargs['base_context']
    return render_to_response('list_category.html', context)


def article_by_category(request, **kwargs):
    context = kwargs['base_context']
    context['category'] = Category.objects.get(name=kwargs['category_name'])
    context['articles'] = Article.objects.all().filter(article_categories=context['category'].id).order_by('-article_dateCreate')
    return render_to_response('articles_by_category.html', context)


