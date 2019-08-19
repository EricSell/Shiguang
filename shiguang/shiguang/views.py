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
                "url": ip + "/mine/changemineinfo/",
                "msg": "编辑个人信息"
            },
            {
                "url": ip + "/article/article_list/",
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
                "url": ip + "/find1/baikelist/",
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
            {
                "url": ip + "/mine/sendcode/",
                "msg": "短信发送验证码"
            },
            {
                "url": ip + "/mine/msg_login/",
                "msg": "短信验证码登录"
            },
            {
                "url": ip + "/index/login_send_email/",
                "msg": "邮箱发送验证码"
            },
            {
                "url": ip + "/index/login_mail_captcha/",
                "msg": "邮箱验证码登录"
            },
            {
                "url": ip + "/index/login/",
                "msg": "密码登录"
            },
            {
                "url": ip + "/index/register/",
                "msg": "注册"
            },
            {
                "url": ip + "/mine/changepassword/",
                "msg": "更改密码"
            },
            {
                "url": ip + "/find1/search/?keywords=蛋",
                "msg": "搜索"
            },

        ]
    }
    return JsonResponse(data)
