# coding=utf-8
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render_to_response, RequestContext
from django.core.paginator import Paginator
from django.db.models import Q

from article.models import Article
from category.models import Category
from tag.models import Tag


def base_context(view):
    def new_view(request, *args, **kwargs):
        context = {}
        context.update(csrf(request))
        context['fresh_articles'] = Article.objects.all().order_by('-article_dateCreate')
        context['popular_articles'] = Article.objects.filter_by_popularity()
        context['categories'] = Category.objects.all().order_by('title')
        context['tags'] = Tag.objects.all()
        if request.POST:
            username = request.POST.get('login_username', '')
            password = request.POST.get('login_password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
        if request.user.is_authenticated():
            context['user_auth'] = request.user
        kwargs['base_context'] = RequestContext(request, context)
        return view(request, *args, **kwargs)
    return new_view


def requires_login(view):
    def new_view(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
        return view(request, *args, **kwargs)
    return new_view


def index(request, page_num=1, **kwargs):
    context = kwargs['base_context']
    current_page = Paginator(context['fresh_articles'], 3)
    context['fresh_articles'] = current_page.page(page_num)
    return render_to_response('index.html', context)


def search(request, **kwargs):
    context = kwargs['base_context']
    if 'search' in request.GET and request.GET['search']:
        try:
            search_message = ''
            search = request.GET['search']
            result = Article.objects.filter(Q(title__icontains=search) | Q(article_text__icontains=search))
            if not len(result):
                search_message = u'По вашему запросу не найдено ни одной статьи.'
        except:
            result = []
            search_message = u'Извините. В данный момент доступ к базе данных невозможен, попробуйте повторить ваш запрос позже.'
    else:
        result = []
        search_message = u'Вы не ввели данные в строку запроса'
    context['result'] = result
    context['search_message'] = search_message
    return render_to_response('search.html', context)