from django.contrib import admin

from author.models import Author
from Kursach.admin import AutoInsertUserAdmin


class AuthorAdmin(AutoInsertUserAdmin):
    fields = ('author_nameFirst', 'author_nameLast', 'author_wiki',)
    list_display = ('author_nameFirst', 'author_nameLast', 'author_wiki', 'get_quantity_articles')
    search_fields = ('author_nameFirst', 'author_nameLast',)


admin.site.register(Author, AuthorAdmin)