# coding=utf-8
from django.db import models

from Kursach.translit import transliterate
from customuser.models import CustomUser
from article.models import Article

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'название', unique=True)
    name = models.CharField(max_length=100, verbose_name=u'отображение URL', unique=True,  blank=True, null=True)
    category_wiki = models.URLField(verbose_name=u'Wiki', blank=True)

    user = models.ForeignKey('customuser.CustomUser', blank=True, null=True, verbose_name=u'пользователь')

    class Meta:
        db_table = 'Category'
        verbose_name = u'категорию'
        verbose_name_plural = u'категории'

    def get_quantity_articles(self):
        articles = Article.objects.filter(article_categories=self.id)
        return len(articles)
    get_quantity_articles.short_description = u'количество статей'

    def get_absolute_url(self):
        return u'категория/{0}/'.format(self.name)

    def __unicode__(self):
        return u'{0}'.format(self.title)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """Переопределение родительского метода, для автоматического ПОВЫШЕНИЯ счётчиков связанных моделей"""
        self.name = self.title.replace(' ', '_').capitalize()
        super(Category, self).save()
