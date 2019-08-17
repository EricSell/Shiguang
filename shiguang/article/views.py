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


# 文章喜欢
def article_like(request):
    user = request.user
    if not user:
        return JsonResponse({"code": 1002, "msg": "用户未登录"})
    article_id = request.GET.get('article_id', False)
    if not article_id:
        return JsonResponse({"code": 1001, "msg": "参数错误"})
    a_like = ArticleLike.objects.filter(article_id=article_id)
    print(user)
    # 如果喜欢表里面没有数据，就新增
    if not a_like.exists():
        a_like = ArticleLike()
        a_like.article_id = article_id
        a_like.user = user
        a_like.save()
        data = {
            "code": 1,
            "msg": "添加到喜欢",
            "is_like": 1,
        }
        return JsonResponse(data)
    else:
        a_like.delete()
        data = {
            "code": 1,
            "msg": "取消喜欢",
            "is_like": 0,
        }
        return JsonResponse(data)
