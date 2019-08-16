from django.db import models


# Create your models here.


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


# 关注表
class Follow(models.Model):
    id = models.IntegerField(primary_key=True)
    myid = models.ForeignKey(User, models.DO_NOTHING, related_name="myid")
    yid = models.ForeignKey(User, models.DO_NOTHING, related_name="yid")

    class Meta:
        db_table = 'follow'
        verbose_name = '关注'
        verbose_name_plural = verbose_name
