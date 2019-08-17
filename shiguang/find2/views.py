from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from find1.models import Baike, BaikeShowLike


# 百科详情
def baike_detail(request):
    if request.method == "GET":
        baikeid = request.GET.get('baikeid')
        # 百科的关注数量与收藏数量
        love_sum=0
        collect_sum=0
        baike_love_coll_sum = BaikeShowLike.objects.filter(baike_id=baikeid)
        if baike_love_coll_sum.exists():
            love_sum = baike_love_coll_sum.filter(love=True).count()
            collect_sum = baike_love_coll_sum.filter(collect=True).count()

        # 用户是否关注
        # user = request.user
        # userid = user.id
        userid = 1
        if userid:
            user_love = int(BaikeShowLike.objects.filter(user_id=userid).first().love)
            user_collect = int(BaikeShowLike.objects.filter(user_id=userid).first().collect)

        # 获取百科详情
        baikes = Baike.objects.filter(id=baikeid)
        if baikes.exists():
            print(baikes)
            baike = baikes.first()
            print(baike)
            baike_name = baike.name
            baike_detail = baike.content
            baike_img = baike.img
            baike_content = {
                'baike_name': baike_name,
                'baike_detail': baike_detail,
                'baike_love': love_sum,
                'baike_collect': collect_sum,
                'baike_img': baike_img,
                'user_love':user_love,
                'user_collect':user_collect,
            }
            data = {
                'code': 0,
                'msg': 'ok',
                'data': {
                    'baike_content': baike_content,
                }
            }
            return JsonResponse(data)

        else:
            return JsonResponse({
                'code': 1002,
                'msg': '没有这篇文章',
            })
    return JsonResponse({
        'code': 1003,
        'msg': '请求方式有误',
    })


# 百科详情喜欢
def baike_detail_love(request):
    if request.method == "GET":

        # user = request.user
        user=1
        baikeid = request.GET.get('baikeid')
        print(baikeid)
        if user:
            if Baike.objects.filter(id=baikeid).first():
                # userid = user.id
                userid = 1
                is_love = BaikeShowLike.objects.filter(user_id=userid, baike_id=baikeid,love=True).first()
                love = BaikeShowLike.objects.filter(user_id=userid, baike_id=baikeid).first()
                if love:
                    if is_love:
                        love.love = 0
                        love.save()
                    else:
                        love.love = 1
                        love.save()
                    return JsonResponse({
                        'code': 0,
                        'msg': 'ok',
                        'data': {
                            'is_love': love.love,
                        }
                    })
                else:
                    print(userid,baikeid)
                    baikeshoulike = BaikeShowLike()
                    baikeshoulike.love = 1
                    baikeshoulike.collect = 0
                    baikeshoulike.user_id = userid
                    baikeshoulike.baike_id = baikeid
                    baikeshoulike.save()
                    return JsonResponse({
                        'code':1001,
                        'msg':'添加数据成功',
                    })
            else:
                return JsonResponse({
                    'code': 1002,
                    'msg': '没有这篇文章',
                })
        else:
            return JsonResponse({
               'code': 1004,
               'msg': '用户未登录',
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
        print(baikeid)
        if user:
            if Baike.objects.filter(id=baikeid).first():
                # userid = user.id
                userid = 1
                is_collect = BaikeShowLike.objects.filter(user_id=userid, baike_id=baikeid, collect=True).first()
                collect = BaikeShowLike.objects.filter(user_id=userid, baike_id=baikeid).first()
                if collect:
                    if is_collect:
                        collect.collect = 0
                        collect.save()
                    else:
                        collect.collect = 1
                        collect.save()
                    return JsonResponse({
                        'code': 0,
                        'msg': 'ok',
                        'data': {
                            'is_collect': collect.collect,
                        }
                    })
                else:
                    print(userid, baikeid)
                    baikeshoulike = BaikeShowLike()
                    baikeshoulike.love = 0
                    baikeshoulike.collect = 1
                    baikeshoulike.user_id = userid
                    baikeshoulike.baike_id = baikeid
                    baikeshoulike.save()
                    return JsonResponse({
                        'code': 1001,
                        'msg': '添加数据成功',
                    })
            else:
                return JsonResponse({
                    'code': 1002,
                    'msg': '没有这篇文章',
                })
        else:
            return JsonResponse({
                'code': 1004,
                'msg': '用户未登录',
            })

    else:
        return JsonResponse({
            'code': 1003,
            'msg': '请求方式有误',
        })


# 用户列表
def user_list(request):
    pass
