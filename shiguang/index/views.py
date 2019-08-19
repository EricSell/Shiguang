import os

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse

# 主页
from find1.models import *
from index.models import *
from utils.mail import send_email

'''
def index(request):
    userid = request.session.get('user_id',0)
    user = User.objects.filter(id=userid).first()
    if user:
        # 用户已登录
        data = {
            'code':1,
            'msg':'susses',
            'data':{
                'user':user.id,
            }
        }
        return JsonResponse(data)
    else:
        # 用户未登录
        data = {
            'code': 1002,
            'msg': 'user not login',
        }
        return JsonResponse(data)
'''


# login
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # 登录
        user = User.objects.filter(email=email).first()
        if user:
            if password == user.password:
                # 用户和密码都匹配
                # 登录成功
                # 加入session
                request.session['user_id'] = user.id

                # 编辑返回的JSON数据
                data = {
                    'code': 1,
                    'msg': 'login_success',
                    'data': {
                        'session': request.session.get('user_id'),
                        'email': user.email,
                    }
                }

                return JsonResponse(data)

            # 编辑返回的JSON数据
            else:
                data = {
                    'code': 1001,
                    'msg': 'email or password Error',
                }
            return JsonResponse(data)

        else:
            # 编辑返回的JSON数据
            data = {
                'code': -1,
                'msg': 'is email not have',
                'data': {
                    'email': email
                }
            }
        return JsonResponse(data)
    else:
        # 编辑返回的JSON数据
        data = {
            'code': -1,
            'msg': '请求错误',
            'data': {
                'method': 'Need POST'
            }
        }
    return JsonResponse(data)


# register
def register(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        email = request.POST.get('email')
        username = request.POST.get('username')
        # 邮箱是否重复
        users = User.objects.filter(email=email)
        if users.exists():
            data = {
                'code': -1,
                'msg': 'email_Repeat'
            }
            return JsonResponse(data)

        # 添加用户信息
        try:
            user = User()
            user.password = password
            user.email = email
            user.username = username
            user.save()

            # 编辑返回的JSON数据
            data = {
                'code': 1,
                'msg': 'add user success',
                'data': {
                    'userid': user.id,
                    'email': user.email,
                }
            }
            return JsonResponse(data)
        except:
            # 编辑返回的JSON数据
            data = {
                'code': -1,
                'msg': 'adduser_fail',
                'data': {
                    'save': 'save fail'
                }
            }
            return JsonResponse(data)

    else:
        # 编辑返回的JSON数据
        data = {
            'code': 1003,
            'msg': '请求错误',
            'data': {
                'method': 'Need POST',
            }
        }
        return JsonResponse(data)


# logout
def logout(request):
    try:
        request.session.delete('user_id')
        request.session.flush()

        data = {
            'code': '1',
            'msg': 'logout_success',
        }
        return JsonResponse(data)
    except:
        data = {
            'code': '-1',
            'msg': 'logout_fail',
        }
        return JsonResponse(data)


# 通过邮箱登录
def login_send_email(request):
    if request.method == "POST":
        email = request.POST.get("email")
        is_email = User.objects.filter(email=email)
        if is_email.exists():
            if cache.get(email, 0):
                return JsonResponse({
                    'code': 1007,
                    'msg': '180内不能重复发送',
                })
            else:
                send = send_email(email)
                if send:
                    return JsonResponse({
                        'code': 1,
                        'msg': 'success',
                    })
                else:
                    return JsonResponse({
                        'code': 1005,
                        'msg': '服务器正忙'
                    })
        else:
            return JsonResponse({
                'code': 1004,
                'msg': '用户未注册',
            })
    else:
        return JsonResponse({
            'code': 1003,
            'msg': '请求方式错误'
        })


# 验证邮箱验证码
def login_mail_captcha(request):
    if request.method == "POST":
        captcha = request.POST.get("captcha")
        try:
            captcha = int(captcha)
        except:
            return JsonResponse({
                'code': 1001,
                'msg': '参数错误',
            })
        email = request.POST.get('email')
        cache_captcha = cache.get(email, 0)
        user = User.objects.filter(email=email).first()
        if not user:
            return JsonResponse({"code": 1004, "msg": "用户未注册"})
        if int(captcha) == int(cache_captcha):
            request.session['user_id'] = user.id
            return JsonResponse({
                'code': 1,
                'msg': 'success',
            })
        else:
            return JsonResponse({
                'code': 1006,
                'msg': '验证码错误',
            })
    else:
        return JsonResponse({
            'code': 1003,
            'msg': '请求方式错误',
        })


# 菜谱列表
def Menu_list(request):
    if request.method == 'GET':
        try:
            m_list = Menu.objects.all()
            z_list = []
            if m_list.exists():
                for menu in m_list:
                    icon = User.objects.get(id=menu.user_id).icon
                    t = {
                        "name": menu.name,
                        "descript": menu.descript,
                        'img': menu.img,
                        'icon': icon
                    }
                    z_list.append(t)

                data = {
                    'code': 1,
                    'msg': 'success',
                    'data': z_list
                }
            else:
                data = {
                    'code': -1,
                    'msg': '无菜谱数据',
                }
        except:
            data = {
                'code': -1,
                'msg': 'get fail'
            }
    else:
        data = {
            'code': 1003,
            'msg': 'method fail'
        }
    return JsonResponse(data)


# 菜谱详情
def Menu_details(request):
    z_user = request.user
    if not z_user:
        return JsonResponse({'code': -1, 'msg': 'user not login'})
    if request.method == 'GET':
        id = request.GET.get('id')
        sid = request.session.get('userid')
        print(sid)
        try:
            # 得到菜谱
            menu = Menu.objects.get(id=id)
            if menu:
                # 得到上传菜谱的用户
                userid = menu.user_id
                user = User.objects.get(id=userid)
                # 获取该菜谱的喜欢与收藏总数
                munu_live = MenuShouLike.objects.filter(menu_id=menu.id, love=1).count()
                munu_collect = MenuShouLike.objects.filter(menu_id=menu.id, collect=1).count()

                # 得到当前用户(session)对此菜谱的喜欢与收藏
                is_live_collect = MenuShouLike.objects.filter(menu_id=menu.id, user_id=sid).first()

                if is_live_collect:
                    data = {
                        'code': 1,
                        'msg': 'success',
                        'data': {
                            'name': menu.name,
                            'descript': menu.descript,
                            'content': menu.content,
                            'img': menu.img,
                            'user_icon': user.icon,
                            'username': user.username,
                            'live': munu_live,
                            'collect': munu_collect,
                            'islive': is_live_collect.love,
                            'iscollect': is_live_collect.collect,
                        }
                    }

                else:
                    data = {
                        'code': 1,
                        'msg': 'success',
                        'data': {
                            'name': menu.name,
                            'descript': menu.descript,
                            'content': menu.content,
                            'img': menu.img,
                            'user_icon': user.icon,
                            'username': user.username,
                            'live': munu_live,
                            'collect': munu_collect,
                            'islive': 0,
                            'iscollect': 0,
                        }
                    }
        except:
            data = {
                'code': 1001,
                'msg': 'get menu details fail',
            }
    else:
        data = {
            'code': 1003,
            'msg': 'method fail'
        }
    return JsonResponse(data)


# 点击喜欢
def cleck_live(request):
    z_user = request.user
    if not z_user:
        return JsonResponse({'code': -1, 'msg': 'user not login'})
    if request.method == 'GET':

        # 获取菜谱id
        menuid = request.GET.get('id')
        # 获取当前用户id
        userid = request.session.get('userid')
        print(userid)
        is_love_collect = MenuShouLike.objects.filter(user_id=userid, menu_id=menuid).first()
        print('v')
        # print(is_love_collect.user_id)
        # 如果表中存在该用户的记录，更改love
        print(is_love_collect)
        if is_love_collect:
            if is_love_collect.love == 1:
                print("a")
                is_love_collect.love = 0
                is_love_collect.save()
            elif is_love_collect.love == 0:
                print("b")
                is_love_collect.love = 1
                is_love_collect.save()

            count = MenuShouLike.objects.filter(menu_id=menuid, love=1).count()
            data = {
                'code': 1,
                'msg': 'success',
                'data': {
                    'love': count,
                    'islove': is_love_collect.love,
                }
            }
            print("AAAAAAAAAA")
        else:
            # 表中没有该用户记录
            try:
                menu_love = MenuShouLike()
                menu_love.love = 1
                menu_love.collect = 0
                menu_love.user_id = userid
                menu_love.menu_id = menuid
                print("a")
                menu_love.save()
                count = MenuShouLike.objects.filter(menu_id=menuid, love=1).count()
                print("aaaaa")
                data = {
                    'code': 1,
                    'msg': 'add love success',
                    'data': {
                        'love': count,
                        'islove': 1,
                    }
                }
            except:
                # 添加喜欢失败
                data = {
                    'code': -1,
                    'msg': 'add love fail',
                }
    else:
        data = {
            'code': 1003,
            'msg': 'method fail'
        }
    return JsonResponse(data)


# 点击收藏
def cleck_collect(request):
    if request.method == 'GET':

        # 获取菜谱id
        menuid = request.GET.get('id')
        # 获取当前用户id
        userid = request.session.get('userid')
        print(userid)
        is_love_collect = MenuShouLike.objects.filter(user_id=userid, menu_id=menuid).first()
        print('v')
        # print(is_love_collect.user_id)
        # 如果表中存在该用户的记录，更改collect
        print(is_love_collect)
        if is_love_collect:
            if is_love_collect.collect == 1:
                print("a")
                is_love_collect.collect = 0
                is_love_collect.save()
            elif is_love_collect.collect == 0:
                print("b")
                is_love_collect.collect = 1
                is_love_collect.save()

            count = MenuShouLike.objects.filter(menu_id=menuid, collect=1).count()
            data = {
                'code': 1,
                'msg': 'success',
                'data': {
                    'count': count,
                    'islove': is_love_collect.collect,
                }
            }
            print("AAAAAAAAAA")
        else:
            # 表中没有该用户记录
            try:
                menu_collect = MenuShouLike()
                menu_collect.love = 0
                menu_collect.collect = 1
                menu_collect.user_id = userid
                menu_collect.menu_id = menuid
                menu_collect.save()
                print("a")
                count = MenuShouLike.objects.filter(menu_id=menuid, collect=1).count()
                print("aaaaa")
                data = {
                    'code': 1,
                    'msg': 'add collect success',
                    'data': {
                        'collect': count,
                        'iscollect': 1,
                    }
                }

            except:
                # 添加收藏失败
                data = {
                    'code': -1,
                    'msg': 'add collect fail',
                }
    else:
        data = {
            'code': 1003,
            'msg': 'method fail'
        }
    return JsonResponse(data)
