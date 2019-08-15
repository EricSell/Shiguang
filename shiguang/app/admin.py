from django.contrib import admin
from app.models import *


# 文章管理
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'name', 'time', 'user']
    list_per_page = 10  # 每页显示的数量
    ordering = ('-time',)  # 排序
    list_editable = ['title', 'user']  # 可编辑的
    search_fields = ['title']  # 可搜索的


# 百科管理
@admin.register(Baike)
class BaikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user']
    list_per_page = 10
    list_editable = ['name', "user"]
    search_fields = ['name']


# 百科收藏喜欢管理
@admin.register(BaikeShowLike)
class BaikeShowLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'baike', 'love', 'collect']
    list_per_page = 10
    list_editable = ['love', 'collect']
    search_fields = ['user', 'baike']


# 用户关注表
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['id', 'myid', 'yid']
    list_per_page = 10
    list_editable = ['myid', 'yid']
    search_fields = ['myid', 'yid']


# 饮食类型管理
@admin.register(Foodtype)
class FoodtypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'menu']
    list_per_page = 10
    search_fields = ['name', 'menu']


# 菜谱管理器
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'time', 'user', 'type']
    list_per_page = 10
    list_editable = ['user', 'type', 'name']
    search_fields = ['name', 'type', 'user']


# 菜谱收藏喜欢管理
@admin.register(MenuShouLike)
class MenuShouLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'menu', 'love', 'collect']
    list_editable = ['love', 'collect']
    list_per_page = 10
    search_fields = ['user', 'menu']


# 菜谱分类管理
@admin.register(Menutype)
class MenutypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'typename']
    list_per_page = 10
    list_editable = ['typename']
    search_fields = ['typename']


# 其他分类管理
@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'menu']
    list_editable = ['menu']
    list_per_page = 10
    search_fields = ['name', 'menu']


# 食材管理
@admin.register(Shicai)
class ShicaiAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'menu']
    list_editable = ['menu']
    list_per_page = 10
    search_fields = ['name', 'menu']


# 主题分类
@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'menu']
    list_editable = ['menu']
    list_per_page = 10
    search_fields = ['name', 'menu']


# 用户管理
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone']
    list_per_page = 10
    list_editable = ['username']
    search_fields = ['username', 'email', 'phone']
