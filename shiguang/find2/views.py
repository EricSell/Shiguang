from django.http import HttpResponse, JsonResponse
from find1.models import Baike, BaikeShowLike, Menu, MenuShouLike
from index.models import User, Follow

# 百科详情
def baike_detail(request):
    if request.method == "GET":
        baikeid = request.GET.get('baikeid')
        # 百科的关注数量与收藏数量
        love_sum = 0
        collect_sum = 0
        baike_love_coll_sum = BaikeShowLike.objects.filter(baike_id=baikeid)
        if baike_love_coll_sum.exists():
            love_sum = baike_love_coll_sum.filter(love=True).count()
            collect_sum = baike_love_coll_sum.filter(collect=True).count()

        # 用户是否关注
        # user = request.user
        # userid = user.id
        userid = 4
        if userid:
            user = BaikeShowLike.objects.filter(user_id=userid)
            if user:
                user_love = int(user.first().love)
                user_collect = int(user.first().collect)
            else:
                user_love = 0
                user_collect = 0

        # 获取百科详情
        baikes = Baike.objects.filter(id=baikeid)
        if baikes.exists():
            baike = baikes.first()
            baike_name = baike.name
            baike_detail = baike.content
            baike_img = baike.img
            baike_content = {
                'baike_name': baike_name,
                'baike_detail': baike_detail,
                'baike_love': love_sum,
                'baike_collect': collect_sum,
                'baike_img': baike_img,
                'user_love': user_love,
                'user_collect': user_collect,
            }
            data = {
                'code': 1,
                'msg': 'ok',
                'data': {
                    'baike_content': baike_content,
                }
            }
            return JsonResponse(data)

        else:
            return JsonResponse({
                'code': 1001,
                'msg': '参数错误',
            })
    return JsonResponse({
        'code': 1003,
        'msg': '请求方式有误',
    })


# 百科详情喜欢
def baike_detail_love(request):
    if request.method == "GET":

        # user = request.user
        user = 1
        baikeid = request.GET.get('baikeid')
        if user:
            if Baike.objects.filter(id=baikeid).first():
                # userid = user.id
                userid = 1
                is_love = BaikeShowLike.objects.filter(user_id=userid, baike_id=baikeid, love=True).first()
                love = BaikeShowLike.objects.filter(user_id=userid, baike_id=baikeid)
                if love.exists():
                    love = love.first()
                    if is_love:
                        love.love = 0
                        love.save()
                    else:
                        love.love = 1
                        love.save()
                    return JsonResponse({
                        'code': 1,
                        'msg': 'ok',
                        'data': {
                            'is_love': love.love,
                        }
                    })
                else:
                    baikeshoulike = BaikeShowLike()
                    baikeshoulike.love = 1
                    baikeshoulike.collect = 0
                    baikeshoulike.user_id = userid
                    baikeshoulike.baike_id = baikeid
                    baikeshoulike.save()
                    return JsonResponse({
                        'code': 1,
                        'msg': '添加数据成功',
                        'data': baikeshoulike.love,
                    })
            else:
                return JsonResponse({
                    'code': 1001,
                    'msg': '参数错误',
                })
        else:
            return JsonResponse({
                'code': 1002,
                'msg': '未登录',
            })

    else:
        return JsonResponse({
            'code': 1003,
            'msg': '请求方式有误',
        })


# 百科详情收藏
def baike_detail_collect(request):
    if request.method == "GET":

        # user = request.user
        user = 1
        baikeid = request.GET.get('baikeid')
        if user:
            if Baike.objects.filter(id=baikeid).first():
                # userid = user.id
                userid = 1
                is_collect = BaikeShowLike.objects.filter(user_id=userid, baike_id=baikeid, collect=True).first()
                collect = BaikeShowLike.objects.filter(user_id=userid, baike_id=baikeid)
                if collect.exists():
                    collect = collect.first()
                    if is_collect:
                        collect.collect = 0
                        collect.save()
                    else:
                        collect.collect = 1
                        collect.save()
                    return JsonResponse({
                        'code': 1,
                        'msg': 'ok',
                        'data': {
                            'is_collect': collect.collect,
                        }
                    })
                else:
                    baikeshoulike = BaikeShowLike()
                    baikeshoulike.love = 0
                    baikeshoulike.collect = 1
                    baikeshoulike.user_id = userid
                    baikeshoulike.baike_id = baikeid
                    baikeshoulike.save()
                    return JsonResponse({
                        'code': 1,
                        'msg': '添加数据成功',
                        'data': baikeshoulike.collect,
                    })
            else:
                return JsonResponse({
                    'code': 1001,
                    'msg': '参数错误',
                })
        else:
            return JsonResponse({
                'code': 1002,
                'msg': '未登录',
            })
    else:
        return JsonResponse({
            'code': 1003,
            'msg': '请求方式有误',
        })


# 用户列表
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        user_list = []
        if users.exists():
            for user in users:
                user_id = user.id
                user_name = user.username
                user_icon = user.icon
                user_content = {
                    'user_id': user_id,
                    'user_name': user_name,
                    'user_icon': user_icon,
                }
                user_list.append(user_content)
            data = {
                'code': 1,
                'msg': 'ok',
                'data': {
                    'user_content': user_list,
                }
            }
            return JsonResponse(data)
    else:
        return JsonResponse({
            'code': 1003,
            'msg': '请求方式有误',
        })


# 用户详情
def user_detail(request):
    if request.method == "GET":
        otherid = request.GET.get('otherid')
        try:
            otherid = int(otherid)
        except:
            return JsonResponse({
                'code': 1001,
                'msg': '参数错误',
            })
        other = User.objects.filter(id=otherid)
        if other:
            # 用户的关注数量与粉丝数量
            other_name = other.first().username
            other_img = other.first().icon
            other_intro = other.first().intro
            fans_sum = Follow.objects.filter(yid_id=otherid).count()
            collect_sum = Follow.objects.filter(myid_id=otherid).count()

            other_detail = {
                'other_name': other_name,
                'other_img': other_img,
                'other_intro': other_intro,
                'fans_sum': fans_sum,
                'collect_sum': collect_sum,

            }

            # 菜谱书与喜欢
            menu_collect = []
            menu_id = MenuShouLike.objects.filter(user_id=otherid, collect=True).values('menu_id')
            menu_id_list = list(menu_id)
            for menu_id in menu_id_list:
                menu_id = int(menu_id.get('menu_id'))
                menu_name = Menu.objects.filter(id=menu_id).first().name
                menu_img = Menu.objects.filter(id=menu_id).first().img
                menu_content = {
                    'menu_id': menu_id,
                    'menu_name': menu_name,
                    'menu_img': menu_img,
                }
                menu_collect.append(menu_content)
            menu_love = []
            menu_id = MenuShouLike.objects.filter(user_id=otherid, love=True).values('menu_id')
            menu_id_list = list(menu_id)
            for menu_id in menu_id_list:
                menu_id = int(menu_id.get('menu_id'))
                menu_name = Menu.objects.filter(id=menu_id).first().name
                menu_img = Menu.objects.filter(id=menu_id).first().img
                menu_content = {
                    'menu_id': menu_id,
                    'menu_name': menu_name,
                    'menu_img': menu_img,
                }
                menu_love.append(menu_content)

            return JsonResponse({
                'code': 1,
                'msg': 'ok',
                'data': {
                    'other_detail': other_detail,
                    'menu_collect': menu_collect,
                    'menu_love': menu_love,
                }
            })
        else:
            return JsonResponse({
                'code': 1001,
                'msg': '参数错误',
            })
    return JsonResponse({
        'code': 1003,
        'msg': '请求方式有误',
    })


# 用户详情-关注
def user_detail_follow(request):
    if request.method == "GET":

        # user = request.user
        user = 1
        if user:
            otherid = request.GET.get('otherid')
            try:
                otherid = int(otherid)
            except:
                return JsonResponse({
                    'code': 1001,
                    'msg': '参数错误',
                })
            if User.objects.filter(id=otherid).first():
                # userid = user.id
                userid = 1
                flag = 0
                follow = Follow.objects.filter(myid_id=userid, yid_id=otherid).first()
                if follow:
                    follow.delete()
                    flag = 0
                else:
                    follow = Follow()
                    follow.myid_id = userid
                    follow.yid_id = otherid
                    follow.save()
                    flag = 1
                return JsonResponse({
                    'code': 1,
                    'msg': 'success',
                    'data': {
                        'is_follow': flag,
                    }
                })
            else:
                return JsonResponse({
                    'code': 1001,
                    'msg': '参数错误',
                })
        else:
            return JsonResponse({
                'code': 1002,
                'msg': '未登录',
            })

    else:
        return JsonResponse({
            'code': 1003,
            'msg': '请求方式有误',
        })
