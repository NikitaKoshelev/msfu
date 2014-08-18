# coding=utf-8
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from article.models import Article
from .models import Likes

# Create your views here.


def likes(request, **kwargs):
    context = kwargs['base_context']
    article = Article.objects.get(name=kwargs['article_name'])
    like_users = set(Likes.objects.filter(likes_article=article).values_list('likes_user', flat=True))
    user = context['user_auth']
    if user != article.user and user.id not in like_users:
        Likes(likes_user=user, likes_article=article).save()
    return HttpResponseRedirect(request.path[:-len('♥')])


def dislikes(request, **kwargs):
    context = kwargs['base_context']
    article = Article.objects.get(name=kwargs['article_name'])
    like_users = Likes.objects.filter(likes_article=article).values_list('likes_user', flat=True)
    user = context['user_auth']
    if user.id in like_users:
        try:
            Likes.objects.get(likes_user=user, likes_article=article).delete()
        except:
            pass
    return HttpResponseRedirect(request.path[:-len('dis♥')])