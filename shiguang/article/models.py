from django.db import models


# Create your models here.
# 文章表
from mdeditor.fields import MDTextField

from index.models import User


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name="标题")
    descript = models.CharField(max_length=200, verbose_name="简介")
    img = models.CharField(max_length=255, verbose_name="文章图片")
    content = MDTextField(blank=True, null=True, verbose_name="内容")
    time = models.TimeField(auto_now_add=True, verbose_name="时间")
    user = models.ForeignKey(User, models.DO_NOTHING, verbose_name="作者")

    class Meta:
        db_table = 'Article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 文章喜欢表
class ArticleLike(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, verbose_name="用户")
    article = models.ForeignKey(Article, models.DO_NOTHING, verbose_name="文章")

    class Meta:
        db_table = 'article_like'
        verbose_name = '文章喜欢表'
        verbose_name_plural = verbose_name
