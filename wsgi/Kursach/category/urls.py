# coding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
from Kursach.views import base_context
from category.views import *

admin.autodiscover()

urlpatterns = patterns('',
                       #url(r'categories/', BaseList.as_view(template_name='list_category.html')),
                       url(r'^$', base_context(list_categories)),
                       #url(r'category/(?P<category_name>\w+)', base_context(article_by_category)),
                       url(ur'^(?P<category_name>\w+)/$', base_context(article_by_category)),
                       url(ur'^(?P<category_name>\w+)/статья/', include('article.urls')),
                       )
