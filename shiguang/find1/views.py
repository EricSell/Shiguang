from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from find1.models import *


def menutype_list(request):
    mtype_list = list(Menutype.objects.all().values("id", "typename", 'menu__img'))
    data = {
        "code": 1,
        "msg": "success",
        "data": mtype_list
    }
    return JsonResponse(data)


def menu_list(request):
    type_id = request.GET.get("type_id")
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

