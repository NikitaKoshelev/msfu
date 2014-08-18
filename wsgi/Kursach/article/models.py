# coding=utf-8
from django.db import models

from ckeditor.fields import RichTextField

from likes.models import Likes
from comment.models import CommentParent


class PopularManager(models.Manager):
    def filter_by_popularity(self, *args, **kwargs):
        """ Раширение objects.filter() сортировкой по популярности"""
        articles = {}
        for article in super(PopularManager, self).get_queryset().filter(*args, **kwargs):
            articles[article] = article.get_quantity_likes()
        reverse_keys = sorted(articles, lambda x, y: cmp(int(articles[x]), int(articles[y])), reverse=True)
        popular_articles = []
        for k in reverse_keys:
            popular_articles.append(k)
        return popular_articles[:5]


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'название', unique=True)
    name = models.CharField(max_length=100, verbose_name=u'отбражение URL', unique=True, blank=True, null=True)
    article_text = RichTextField(verbose_name=u'текст статьи')
    article_dateCreate = models.DateTimeField(auto_now_add=True, verbose_name=u'дата создания', blank=False)
    article_preview = models.ImageField(upload_to='article_preview', verbose_name=u'превью', blank=True)

    user = models.ForeignKey('customuser.CustomUser', blank=True, null=True, verbose_name=u'пользователь')
    article_authors = models.ManyToManyField('author.Author', verbose_name=u'авторы')
    article_categories = models.ManyToManyField('category.Category', verbose_name=u'категории')
    article_tags = models.ManyToManyField('tag.Tag', verbose_name=u'теги')

    class Meta:
        db_table = 'Article'
        verbose_name = u'статью'
        verbose_name_plural = u'статьи'

    def get_tags(self):
        """Возвращает список ManyToMany для поля article_tags"""
        tags_list = self.article_tags.get_query_set()
        tags_str = ''
        for tag in tags_list:
            tags_str += ', ' + tag.title
        return tags_str.lstrip(', ')
    get_tags.short_description = 'тег(и)'
    
    def get_categories(self):
        """Возвращает список ManyToMany для поля categories"""
        categories_list = self.article_categories.get_query_set()
        categories_str = ''
        for category in categories_list:
            categories_str += ', ' + category.title
        return categories_str.lstrip(', ')
    get_categories.short_description = 'категория(и)'
    
    def get_authors(self):
        """Возвращает список ManyToMany для поля article_authors"""
        authors_list = self.article_authors.get_query_set()
        authors_str = ''
        for author in authors_list:
            authors_str += ', ' + author.author_nameFirst + ' ' + author.author_nameLast
        return authors_str.lstrip(', ')
    get_authors.short_description = u'автор(ы)'

    def get_quantity_likes(self):
        """Возвращает количество лайков из связанной модели Likes"""
        likes = Likes.objects.filter(likes_article=self.id)
        quantity_likes = len(likes)
        return quantity_likes
    get_quantity_likes.short_description = u'рейтинг'

    def get_quantity_comments(self):
        """Возвращает количество комментариев из связанной модели CommentParent"""
        comments = CommentParent.objects.filter(commentParent_article=self.id)
        quantity_comments = len(comments)
        return quantity_comments
    get_quantity_comments.short_description = u'количество комментариев'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """Переопределение родительского метода,
            для автоматического обновления картинок поля ImageField(article_preview)"""
        self.name = self.title.replace(' ', '_').capitalize()
        try:
            obj = Article.objects.get(id=self.id)
            if obj.article_preview.path != self.article_preview.path:
                obj.article_preview.delete()
        except:
            pass
        super(Article, self).save()

    def delete(self, using=None):
        """Переопределение родительского метода,
            для автоматического удаления картинок для поля ImageField(article_preview)"""
        try:
            obj = Article.objects.get(id=self.id)
            obj.article_preview.delete()
        except (Article.DoesNotExist, ValueError):
            pass
        super(Article, self).delete()

    def get_absolute_url(self):
        return u'/статья/{0}/'.format(self.name)

    def __unicode__(self):
        return self.title

    objects = PopularManager()