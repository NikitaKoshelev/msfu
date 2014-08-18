# coding=utf-8
from django.db import models

# Create your models here.


class Likes(models.Model):
    likes_article = models.ForeignKey('article.Article', verbose_name=u'like')
    likes_user = models.ForeignKey('customuser.CustomUser', verbose_name=u'пользователь')

    class Meta:
        db_table = 'Likes'
        verbose_name = u'like'
        verbose_name_plural = u'likes'
