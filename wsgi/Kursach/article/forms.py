import json

from django.http import HttpResponse
from django.views.generic.edit import *
from article.models import *


class ArticleCreate(CreateView):
    model = Article
    fields = ('title', 'article_preview', 'article_authors', 'article_categories', 'article_tags', 'article_text',)

    class Media:
        css = {
            'all': ('/admin/base.css', '/admin/changelist.css', 'admin/forms.css', 'admin/widgets.css',)
        }
        js = ('actions.js',)
