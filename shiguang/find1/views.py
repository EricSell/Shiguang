from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

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
