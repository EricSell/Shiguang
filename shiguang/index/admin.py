from django.contrib import admin


# Register your models here.
# 用户关注表
from index.models import *


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['id', 'myid', 'yid']
    list_per_page = 10
    list_editable = ['myid', 'yid']
    search_fields = ['myid', 'yid']


# 用户管理
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone']
    list_per_page = 10
    list_editable = ['username']
    search_fields = ['username', 'email', 'phone']
