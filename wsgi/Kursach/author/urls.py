from django.conf.urls import patterns, include, url

from django.contrib import admin
from Kursach.views import base_context
from .views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Kursach.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'$', base_context(list_authors))
)
