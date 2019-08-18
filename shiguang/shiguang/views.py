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
            {
                "url": ip + "/article/articlelike/?article_id=3",
                "msg": "将文章添加到自己喜欢"
            },
            {
                "url": ip + "/find1/menutypelist/",
                "msg": "发现-菜谱"
            },
            {
                "url": ip + "/find1/menulist/?type_id=2",
                "msg": "菜谱分类列表"
            },
            {
                "url": ip + "/find1/baike_list/",
                "msg": "百科列表"
            },
            {
                "url": ip + "/find2/baikedetail/",
                "msg": "百科详情"
            },
            {
                "url": ip + "/find2/baikedetaillove/",
                "msg": "百科详情-喜欢"
            },
            {
                "url": ip + "/find2/baikedetailcollect/",
                "msg": "百科详情-收藏"
            },
            {
                "url": ip + "/find2/userlist/",
                "msg": "用户列表"
            },
            {
                "url": ip + "/find2/userdetail/",
                "msg": "用户详情"
            },
            {
                "url": ip + "/find2/userdetailfollow/",
                "msg": "用户详情-关注"
            },

        ]
    }
    return JsonResponse(data)
