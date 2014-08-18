# coding=utf-8
from django.db import models

from ckeditor.fields import RichTextField


class CommentParent(models.Model):
    commentParent_text = RichTextField(verbose_name=u'Текст комментария')
    commentParent_dateCreate = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания', blank=False)

    commentParent_article = models.ForeignKey('article.Article', blank=True, null=True)
    user = models.ForeignKey('customuser.CustomUser', blank=True, null=True)

    class Meta:
        db_table = 'CommentParent'
        verbose_name = u'коментарии'
        verbose_name_plural = u'Коментарий'

    def get_commentChild(self):
        commentChild = CommentChild.objects.filter(commentChild_commentParent=self.id)
        return commentChild


class CommentChild(models.Model):
    commentChild_text = RichTextField(verbose_name=u'Текст ответа')
    commentChild_dateCreate = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания', blank=False)

    user = models.ForeignKey('customuser.CustomUser', blank=True, null=True)
    commentChild_commentParent = models.ForeignKey(CommentParent, blank=True, null=True)

    class Meta:
        db_table = 'CommentChild'
        verbose_name = u'ответы'
        verbose_name_plural = u'Ответ'

