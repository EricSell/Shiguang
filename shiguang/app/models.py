# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# 文章表
class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30, verbose_name="标题")
    descript = models.CharField(max_length=200, verbose_name="简介")
    name = models.CharField(max_length=20, verbose_name="文章名字")
    content = models.TextField(blank=True, null=True, verbose_name="内容")
    time = models.TimeField(auto_created=True, verbose_name="时间")
    user = models.ForeignKey('User', models.DO_NOTHING, verbose_name="作者")

    class Meta:
        db_table = 'Article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章喜欢表
class ArticleLike(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, verbose_name="用户")
    article = models.ForeignKey(Article, models.DO_NOTHING, verbose_name="文章")

    class Meta:
        db_table = 'article_like'
        verbose_name = '文章喜欢表'
        verbose_name_plural = verbose_name


# 百科表
class Baike(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="百科名")
    content = models.TextField(verbose_name="内容")
    user = models.ForeignKey('User', models.DO_NOTHING, verbose_name="用户")

    class Meta:
        db_table = 'baike'
        verbose_name = '百科'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 百科喜欢收藏表
class BaikeShowLike(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, verbose_name="用户")
    baike = models.ForeignKey(Baike, models.DO_NOTHING, verbose_name="百科")
    love = models.BooleanField(default=False, verbose_name="喜欢")
    collect = models.BooleanField(default=False, verbose_name="收藏")

    class Meta:
        db_table = 'baike_show_like'
        verbose_name = '百科喜欢收藏表'
        verbose_name_plural = verbose_name


# 关注表
class Follow(models.Model):
    id = models.IntegerField(primary_key=True)
    myid = models.ForeignKey('User', models.DO_NOTHING, related_name="myid")
    yid = models.ForeignKey('User', models.DO_NOTHING, related_name="yid")

    class Meta:
        db_table = 'follow'
        verbose_name = '关注'
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
    user = models.ForeignKey('User', models.DO_NOTHING, verbose_name="发表人")
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
    user = models.ForeignKey('User', models.DO_NOTHING, verbose_name="用户")
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


# 用户表
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20, verbose_name="昵称")
    password = models.CharField(max_length=20, verbose_name="密码")
    email = models.CharField(max_length=50, unique=True, verbose_name="邮箱")
    phone = models.CharField(max_length=11, unique=True, verbose_name="手机号")
    icon = models.CharField(max_length=255, blank=True, null=True, verbose_name="头像")
    intro = models.TextField(blank=True, null=True, verbose_name="简介")
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'
        verbose_name = '用户表(my)'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
