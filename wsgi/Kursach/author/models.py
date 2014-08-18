# coding=utf-8
from django.db import models

from article.models import Article


class Author(models.Model):
    author_nameFirst = models.CharField(max_length=30, verbose_name=u'Имя')
    author_nameLast = models.CharField(max_length=30, verbose_name=u'Фамилия')
    author_wiki = models.URLField(verbose_name=u'Wiki', blank=True)

    user = models.ForeignKey('customuser.CustomUser', blank=True, null=True, verbose_name=u'пользователь')

    class Meta:
        db_table = 'Author'
        verbose_name = u'автора'
        verbose_name_plural = u'Автор'

    def get_quantity_articles(self):
        articles = Article.objects.filter(article_categories=self.id)
        return len(articles)
    get_quantity_articles.short_description = u'количество статей'

    def __unicode__(self):
        return u'{0} {1}'.format(self.author_nameFirst, self.author_nameLast)

