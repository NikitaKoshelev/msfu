# coding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin

from Kursach.views import base_context
from .views import *
admin.autodiscover()

urlpatterns = patterns('customuser.views',
    # Examples:
    # url(r'^$', 'Kursach.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(ur'Регистрация/$', base_context(create)),
    url(ur'Выход/$', logout),
    #url(r'register/$', base_context(create)),

)
