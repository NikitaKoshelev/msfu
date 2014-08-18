from django.shortcuts import render_to_response, redirect

from article.models import Article
from .forms import CommentChildForm, CommentParentForm, CommentParent
from datetime import datetime
# Create your views here.


def add_commentParent(request, **kwargs):
    context = kwargs['base_context']
    if request.POST:
        form = CommentParentForm(request.POST)
        if form.is_valid():
            commentParent = form.save(commit=False)
            commentParent.user = context['user']
            commentParent.commentParent_dateCreate = datetime.now()
            commentParent.commentParent_article = Article.objects.get(name=kwargs['article_name'])
            form.save()
    return redirect(request.path[:-len('add/commentParent/')])


def add_commentChild(request, **kwargs):
    context = kwargs['base_context']
    context['article'] = Article.objects.get(name=kwargs['article_name'])
    context['commentParents'] = CommentParent.objects.filter(commentParent_article=context['article'].id)
    context['form'] = CommentChildForm(request.POST)
    context = kwargs['base_context']
    if request.user == context['article'].user:
        if request.POST:
            form = CommentChildForm(request.POST)
            if form.is_valid():
                commentChild = form.save(commit=False)
                commentChild.user = context['user']
                commentChild.commentParent_dateCreate = datetime.now()
                commentParent = CommentParent.objects.get(id=int(kwargs['commentParent_id']))
                commentChild.commentChild_commentParent = commentParent
                form.save()
            return redirect(request.path[:-len('commentParent/{0}/add/commentChild/'.format(kwargs['commentParent_id']))])
    return render_to_response('add_child.html', context)