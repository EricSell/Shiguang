from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from index.models import User


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        login_list = ['/mine/mine/', '/mine/changemineinfo/']
        if request.path in login_list:
            user_id = request.session.get("user_id", 0)
            user = User.objects.filter(id=user_id).first()
            request.user = user
            if not user:
                data = {
                    "code": -1,
                    'msg': "没有登录"
                }
                return JsonResponse(data)
