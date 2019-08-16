from django.contrib import admin


# Register your models here.
# 百科管理
from find1.models import *


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
