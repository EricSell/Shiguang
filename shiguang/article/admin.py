from django.contrib import admin

# Register your models here.
# 文章管理
from article.models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'name', 'time', 'user']
    list_per_page = 10  # 每页显示的数量
    ordering = ('-time',)  # 排序
    list_editable = ['title', 'user']  # 可编辑的
    search_fields = ['title']  # 可搜索的