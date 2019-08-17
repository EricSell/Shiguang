from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from find1.models import *
from utils.tools import upload_to_ali


def mine(request):
    # session?
    user = request.user

    if user:
        menu_list = list(Menu.objects.filter(user=user).values("name", 'img'))
        like_list = list(Menu.objects.filter(menushoulike__love=True, user=user).values("name", 'img'))
        data = {
            "code": 1,
            "msg": "success",
            "username": user.username,
            "usericon": user.icon,
            "menu_list": menu_list,
            'like_list': like_list,
        }
        return JsonResponse(data)


def change_mine_info(request):
    if request.method == "GET":
        user = request.user
        if user:
            data = {
                "code": 1,
                "msg": "success",
                "username": user.username,
                "usericon": user.icon,
                "email": user.email,
                "intro": user.intro
            }
            return JsonResponse(data)
        return JsonResponse({
            "code": -1,
            "msg": "没有登录"
        })
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        intro = request.POST.get("intro")

        icon = request.FILES.get("icon")
        print(icon)
        # 图片上传到云服务器
        try:

            user = request.user
            status, url_icon = upload_to_ali(icon)

            if status == 200:
                user.username = username
                user.email = email
                user.intro = intro
                user.icon = url_icon
                user.save()
                data = {
                    "code": 1,
                    "msg": "success",
                    "username": user.username,
                    "usericon": user.icon,
                    "email": user.email,
                    "intro": user.intro
                }
                return JsonResponse(data)
        except:
            return JsonResponse({"code": -1, "msg": "fail"})
