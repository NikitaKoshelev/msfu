# coding=utf-8
from django.shortcuts import render_to_response, redirect

from article.models import Article
from comment.forms import CommentParent, CommentParentForm


def article_detail(request, **kwargs):
    context = kwargs['base_context']
    context['article'] = Article.objects.get(name=kwargs['article_name'])
    context['commentParents'] = CommentParent.objects.filter(commentParent_article=context['article'].id)
    context['form'] = CommentParentForm(request.POST)
    return render_to_response('article_detail.html', context)


