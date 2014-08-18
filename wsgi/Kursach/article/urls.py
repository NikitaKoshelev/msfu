# coding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin

from article.views import *
from Kursach.views import base_context, requires_login


admin.autodiscover()

urlpatterns = patterns('',
                       url(ur'^(?P<article_name>\w+)/$', base_context(article_detail)),
                       url(ur'^(?P<article_name>\w+)/', include('comment.urls')),
                       url(ur'^(?P<article_name>\w+)/', include('likes.urls')),

                       )

