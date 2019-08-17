from django.http import JsonResponse


def index(request):
    ip = "http://106.52.199.168"
    data = {
        "api_list": [
            {
                "url": ip + "/mine/mine",
                "msg": "用户个人信息及菜谱"
            },
            {
                "url": ip + "/mine/minechangeinfo",
                "msg": "编辑个人信息"
            },
            {
                "url": ip + "/article/article_list",
                "msg": "文章列表"
            },
            {
                "url": ip + "/article/article_detail/?article_id=1",
                "msg": "文章详情"
            },
        ]
    }
    return JsonResponse(data)
