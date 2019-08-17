from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from article.models import Article, ArticleLike


# 文章列表
def article_list(request):
    a_list = Article.objects.all()
    if a_list.exists():
        a_list = list(a_list.values("title", 'img', 'descript'))
        data = {
            "code": 1,
            "msg": 'success',
            "data": a_list
        }
    else:
        data = {
            "code": -1,
            "msg": '无文章数据',
        }
    return JsonResponse(data)


# 文章详情
def article_detail(request):
    article_id = request.GET.get("article_id")
    article = Article.objects.filter(id=article_id).first()

    if article:
        like_num = ArticleLike.objects.filter(article=article).count()
        data = {
            "code": 1,
            "msg": "success",
            "data": {
                "article": {
                    "title": article.title,
                    "descript": article.descript,
                    "img": article.img,
                    "content": article.content,
                    "time": article.time,
                    "username": article.user.username,
                    'usericon': article.user.icon,
                    "like_num": like_num,
                }
            }
        }
        return JsonResponse(data)
    return JsonResponse({"code": "-1", "msg": "没有找到数据"})