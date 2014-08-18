from django.conf.urls import patterns, include, url
from Kursach.views import base_context
from django.contrib import admin
from .views import tag_list
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Kursach.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', base_context(tag_list)),
)
