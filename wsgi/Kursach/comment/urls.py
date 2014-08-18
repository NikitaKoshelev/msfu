from django.conf.urls import patterns, include, url

from django.contrib import admin
from Kursach.views import base_context
from .views import add_commentParent, add_commentChild
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Kursach.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add/commentParent/$', base_context(add_commentParent)),
    url(r'^commentParent/(?P<commentParent_id>\d+)/add/commentChild/$', base_context(add_commentChild)),
)
