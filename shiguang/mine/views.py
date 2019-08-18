from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from find1.models import *
from index.models import Follow
from utils.send_msg import send_msg
from utils.tools import upload_to_ali


# 个人中心，菜谱
def mine(request):
    # session?
    user = request.user
    if user:
        menu_list = list(Menu.objects.filter(user=user).values("name", 'img'))
        like_list = list(Menu.objects.filter(menushoulike__love=True, user=user).values("name", 'img'))
        Fan_num = Follow.objects.filter(yid=user.id).count()
        follow_num = Follow.objects.filter(myid=user.id).count()
        data = {
            "code": 1,
            "msg": "success",
            "username": user.username,
            "usericon": user.icon,
            "menu_list": menu_list,
            'like_list': like_list,
            "Fan_num": Fan_num,
            "follow_num": follow_num
        }
        return JsonResponse(data)


# 编辑个人资料
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
            return JsonResponse({"code": -1, "msg": "修改失败"})
    return JsonResponse({"code": -1, "msg": "请求方式错误"})


# 更改密码
def change_password(request):
    user = request.user
    if not user:
        return JsonResponse({"code": 1002, "msg": "用户未登录"})
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        new_password2 = request.POST.get("new_password2")
        if old_password != user.password:
            return JsonResponse({"code": -1, "msg": "当前密码错误"})
        if new_password != new_password2:
            return JsonResponse({"code": -1, "msg": "两次密码不一致"})
        user.password = new_password
        user.save()
        return JsonResponse({"code": 1, "msg": "密码修改成功"})
    return JsonResponse({"code": 1003, "msg": "请求方式错误"})


# 发送短信
def send_code(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        user = User.objects.filter(phone=phone).first()
        is_timeout = cache.get(phone, 0)
        if is_timeout == "0":
            return JsonResponse({"code": -1, "msg": "3分钟之内只能发一次短信"})
        if not user:
            return JsonResponse({"code": 1004, "msg": "用户未注册"})
        status = send_msg(phone)
        if status:
            data = {
                "code": 1,
                "msg": "短信成功"
            }
            return JsonResponse(data)
        return JsonResponse({"code": 1005, "msg": "服务器正忙，发送失败"})
    return JsonResponse({"code": 1003, "msg": "请求方式错误"})


# 短信登录
def msg_login(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        code = request.POST.get("code")
        user = User.objects.filter(phone=phone).first()
        cache_code = cache.get(phone, 0)
        if not user:
            return JsonResponse({"code": 1004, "msg": "用户未注册"})
        if code == cache_code:
            request.session['user_id'] = user.id
            cache.delete(phone)
            data = {
                "code": 1,
                "msg": "登录成功",
            }
            return JsonResponse(data)
        return JsonResponse({"code": 1006, "msg": "验证码错误"})
    return JsonResponse({"code": 1003, "msg": "请求方式错误"})
