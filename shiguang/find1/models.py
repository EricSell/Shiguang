from django.db import models


# Create your models here.
# 百科表
from index.models import User


class Baike(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="百科名")
    content = models.TextField(verbose_name="内容")
    user = models.ForeignKey(User, models.DO_NOTHING, verbose_name="用户")

    class Meta:
        db_table = 'baike'
        verbose_name = '百科'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 百科喜欢收藏表
class BaikeShowLike(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, verbose_name="用户")
    baike = models.ForeignKey(Baike, models.DO_NOTHING, verbose_name="百科")
    love = models.BooleanField(default=False, verbose_name="喜欢")
    collect = models.BooleanField(default=False, verbose_name="收藏")

    class Meta:
        db_table = 'baike_show_like'
        verbose_name = '百科喜欢收藏表'
        verbose_name_plural = verbose_name


# 饮食类型
class Foodtype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="饮食分类名")
    menu = models.ForeignKey('Menu', models.DO_NOTHING, verbose_name="菜谱")

    class Meta:
        db_table = 'foodtype'
        verbose_name = '饮食类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 菜谱
class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name="菜谱名")
    content = models.TextField(verbose_name="内容")
    descript = models.CharField(max_length=200, verbose_name="描述")
    img = models.CharField(max_length=255, blank=True, null=True, verbose_name="图片")
    time = models.TimeField(auto_created=True, verbose_name="时间")
    user = models.ForeignKey(User, models.DO_NOTHING, verbose_name="发表人")
    type = models.ForeignKey('Menutype', models.DO_NOTHING, verbose_name="菜谱类型")

    class Meta:
        db_table = 'menu'
        verbose_name = '菜谱'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 菜谱喜欢收藏表
class MenuShouLike(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, verbose_name="用户")
    menu = models.ForeignKey(Menu, models.DO_NOTHING, verbose_name="菜谱")
    love = models.BooleanField(default=False, verbose_name="喜欢")
    collect = models.BooleanField(default=False, verbose_name="收藏")

    class Meta:
        db_table = 'menu_shou_like'
        verbose_name = '菜谱喜欢收藏表'
        verbose_name_plural = verbose_name


# 菜谱类型
class Menutype(models.Model):
    id = models.IntegerField(primary_key=True)
    typename = models.CharField(max_length=20, verbose_name="菜谱分类")

    class Meta:
        db_table = 'menutype'
        verbose_name = '菜谱类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.typename


# 其他分类
class Other(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="其他分类名")
    menu = models.ForeignKey(Menu, models.DO_NOTHING, verbose_name="菜谱")

    class Meta:
        db_table = 'other'
        verbose_name = '其他分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 食材
class Shicai(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="食材分类名")
    menu = models.ForeignKey(Menu, models.DO_NOTHING, verbose_name="菜谱")

    class Meta:
        db_table = 'shicai'
        verbose_name = "食材"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 主题
class Theme(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="主题分类名")
    menu = models.ForeignKey(Menu, models.DO_NOTHING, verbose_name="菜谱")

    class Meta:
        db_table = 'theme'
        verbose_name = '主题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
