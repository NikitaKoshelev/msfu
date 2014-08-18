from django.contrib import admin

from Kursach.admin import AutoInsertUserAdmin

from .models import CommentParent, CommentChild
from customuser.models import CustomUser
from article.models import Article


class CommentParentAdmin(AutoInsertUserAdmin):
    list_display = ('commentParent_dateCreate',
                    'user',
                    'commentParent_article')

    list_filter = ('commentParent_dateCreate', )

    date_hierarchy = 'commentParent_dateCreate'

    ordering = ('commentParent_dateCreate',)

    search_fields = ('commentParent_text',
                     'commentParent_article',
                     'user__first_name',
                     'user__last_name',
                     'user',)

    fields = ('commentParent_text',
              'commentParent_article', 'commentParent_commentChild')

    def save_model(self, request, obj, form, change):
        super(CommentParentAdmin, self).save_model(request, obj, form, change)
        if form.is_valid():
            if not change:
                article = obj.commentParent_article
                article.article_quantityComments += 1
                article.save()


class CommentChildAdmin(AutoInsertUserAdmin):
    list_display = ('commentChild_dateCreate',
                    'user',
                    'commentChild_commentParent')

    list_filter = ('commentChild_dateCreate', )

    date_hierarchy = 'commentChild_dateCreate'

    ordering = ('commentChild_dateCreate',)

    search_fields = ('commentChild_text',
                     'user',)

    fields = ('commentChild_text',
              'commentChild_commentParent',)

admin.site.register(CommentParent, CommentParentAdmin)
admin.site.register(CommentChild, CommentChildAdmin)
