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
            if cache.get(email,0):
                return JsonResponse({
                    'code':1007,
                    'msg':'180内不能重复发送',
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
            'code':1003,
            'msg':'请求方式错误'
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
        user = User.object.filter(email=email).first()
        if not user:
            return JsonResponse({"code":1004, "msg": "用户未注册"})
        if int(captcha) == int(cache_captcha):
            request.sesseion['user_id'] = user.id
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
    # m_list = Menu.objects

    pass


# 菜谱详情
def Menu_details(request):
    pass
