from django.contrib import admin

from Kursach.admin import AutoInsertUserAdmin

from .models import Category


class CategoryAdmin(AutoInsertUserAdmin):
    list_display = ('title', 'name', 'category_wiki', 'get_quantity_articles')
    fields = ('title', 'category_wiki')
    search_fields = ('title', 'name',)


admin.site.register(Category, CategoryAdmin)