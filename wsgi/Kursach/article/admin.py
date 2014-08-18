from django.contrib import admin

from Kursach.admin import AutoInsertUserAdmin

from .models import Article


class ArticleAdmin(AutoInsertUserAdmin):
    list_display = ('title',
                    'name',
                    'get_quantity_likes',
                    'get_quantity_comments',
                    'article_dateCreate',
                    'user',
                    'get_authors',
                    'get_tags',
                    'get_categories',)

    list_filter = ('article_dateCreate',)
                   #'get_quantity_likes',
                   #'get_quantity_comments',)

    date_hierarchy = 'article_dateCreate'

    ordering = ('article_dateCreate',)
                #'get_quantity_likes',
                #'get_quantity_comments',)

    search_fields = ('title',
                     'user__first_name',
                     'user__last_name',
                     'article_authors__authors_nameFirst',
                     'article_authors__authors_nameLast',)

    fields = ('title',
              'article_preview',
              'article_authors',
              'article_categories',
              'article_tags',
              'article_text',)

    filter_horizontal = ('article_authors',
                         'article_categories',
                         'article_tags',)



admin.site.register(Article, ArticleAdmin)

