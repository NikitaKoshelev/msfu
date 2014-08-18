from django.contrib import admin

from .models import Tag

from Kursach.admin import AutoInsertUserAdmin


class TagAdmin(AutoInsertUserAdmin):
    list_display = ('title', 'name', 'tag_wiki', 'get_quantity_articles', 'user')
    fields = ('title', 'tag_wiki',)
    search_fields = ('title', 'name',)

admin.site.register(Tag, TagAdmin)