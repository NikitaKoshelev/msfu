# coding=utf-8
from django.db import models
from django.contrib.auth.models import User, UserManager
from article.models import Article


class CustomUser(User):
    timezone = models.CharField(max_length=50, default='Europe/Moscow')
    ava = models.ImageField(upload_to='avatars', verbose_name=u'Аватар', blank=True)
    karma = models.IntegerField(default=0, verbose_name=u'Рейтинг', blank=True)
    quantity_topics = models.IntegerField(default=0, verbose_name=u'Количество статей', blank=True)

    objects = UserManager()

    class Meta:
        db_table = 'CustomUser'
        verbose_name = u'профили пользователей'
        verbose_name_plural = u'Профиль пользователя'

    def get_quantity_articles(self):
        articles = Article.objects.filter(article_categories=self.id)
        return len(articles)
    get_quantity_articles.short_description = u'количество статей'

    def get_blog_articles(self):
        popular_articles = Article.objects.filter_by_popularity(user=self.id)
        fresh_articles = Article.objects.filter(user=self.id).order_by('-article_dateCreate')
        return popular_articles, fresh_articles
    get_blog_articles.short_description = u'блог'

    def __unicode__(self):
        return self.username