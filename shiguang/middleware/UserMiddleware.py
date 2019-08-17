from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from index.models import User


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        login_list = ['/mine/mine/', '/mine/changemineinfo/', '/article/articlelike/']
        if request.path in login_list:
            user_id = request.session.get("user_id", 1)
            user = User.objects.filter(id=user_id).first()
            request.user = user
            if not user:
                data = {
                    "code": 1002,
                    'msg': "用户未登录"
                }
                return JsonResponse(data)
