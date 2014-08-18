# coding=utf-8
from django.conf.urls import patterns, url

from django.contrib import admin
from .views import likes, dislikes
from Kursach.views import base_context
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Kursach.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(ur'^♥/$', base_context(likes)),
    url(ur'^dis♥/$', base_context(dislikes)),
)
