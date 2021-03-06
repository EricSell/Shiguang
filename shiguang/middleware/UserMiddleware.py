from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from index.models import User


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        login_list = ['/mine/mine/', '/mine/changemineinfo/', '/article/articlelike/', '/mine/changepassword/',
                      '/find2/baikedetaillove/', '/find2/baikedetailcollect/', '/find2/userdetail/',
                      '/find2/userdetailfollow/', "/index/clecklive/", "/index/cleckcollect/"]
        if request.path in login_list:
            user_id = request.session.get("user_id", 0)
            user = User.objects.filter(id=user_id).first()
            request.user = user
            if not user:
                data = {
                    "code": 1002,
                    'msg': "用户未登录"
                }
                return JsonResponse(data)

    def process_exception(self, exception):
        return JsonResponse({"code": -1, "msg": "别乱搞，请查看详细的api文档"})