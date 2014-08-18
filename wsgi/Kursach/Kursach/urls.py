# coding=utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(ur'^$', 'Kursach.views.home', name='home'),
    # url(ur'^blog/', include('blog.urls')),
    url(ur'^$', base_context(index)),
    url(ur'^page/(?P<page_num>\d+)/$', base_context(index)),
    url(ur'^search/', base_context(search)),
    url(ur'^page/(?P<page_num>\d+)/статья/', include('article.urls')),
    url(ur'^статья/', include('article.urls')),
    url(ur'^Администрирование/', include(admin.site.urls)),
    url(ur'^категория/', include('category.urls')),
    url(ur'^категории/', include('category.urls')),
    url(ur'^блог/', include('blog.urls')),
    url(ur'^автор/', include('author.urls')),
    url(ur'^авторы/', include('author.urls')),
    url(ur'^аккаунт/', include('customuser.urls')),
    url(ur'^аккаунты/', include('customuser.urls')),
    url(ur'^тег/', include('tag.urls')),
    url(ur'^теги/', include('tag.urls')),

)

urlpatterns += patterns('',
    url(ur'^ckeditor/', include('ckeditor.urls')),
    #url(ur'^register/$', 'registration.registeur', {'form': RegistrationFormUniqueEmail}, name='registration_registeur'),
    #url(ur'^accounts/', include('registration.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
