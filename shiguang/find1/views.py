from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from article.models import Article
from find1.models import *


def menutype_list(request):
    # mtype_list1 = Menutype.objects.all()
    mtype_list = list(Menutype.objects.all().values("id", "typename"))
    for i in mtype_list:
        m = Menu.objects.filter(type_id=i['id']).first()
        if m:
            i.update({"img": m.img})
        else:
            i.update({
                "img": "https://wc-blog.oss-cn-beijing.aliyuncs.com/shiguang/u%3D2161734677%2C3732758008%26fm%3D26%26gp%3D0.jpg"})
    data = {
        "code": 1,
        "msg": "success",
        "data": mtype_list
    }
    return JsonResponse(data)


def menu_list(request):
    type_id = request.GET.get("type_id")
    try:
        type_id = int(type_id)
    except:
        return JsonResponse({"code": 1001, "msg": "参数格式错误"})
    type = Menutype.objects.filter(id=type_id).first()

    m_list = list(Menu.objects.filter(type_id=type.id).values("id", "name", "img", "user__username", "user__icon"))
    data = {
        "code": 1,
        "msg": "success",
        "data": m_list
    }
    return JsonResponse(data)


def baike_list(request):
    b_list = list(Baike.objects.all().values("id", "name", "img"))
    data = {
        "code": 1,
        "msg": "success",
        "data": b_list
    }
    return JsonResponse(data)


def search(request):
    if request.method == "GET":
        keywords = request.GET.get("keywords")
        m_list = list(Menu.objects.filter(name__icontains=keywords).values("id", 'img', 'name'))
        a_list = list(Article.objects.filter(title__icontains=keywords).values("id", 'img', 'title'))
        b_list = list(Baike.objects.filter(name__icontains=keywords).values("id", "img", "name"))
        u_list = list(User.objects.filter(username__contains=keywords).values("id", "icon", "username"))

        if not len(m_list):
            m_list = 0
        if not len(a_list):
            a_list = 0
        if not len(b_list):
            b_list = 0
        if not len(u_list):
            u_list = 0

        data = {
            "code": 1,
            "msg": "success",
            "data": {
                "menu_list": m_list,
                "article_list": a_list,
                "baike_list": b_list,
                "user_list": u_list,
            }
        }
        return JsonResponse(data)
    return JsonResponse({"code": 1003, "msg": "请求方式错误"})
