from django.urls import path

from mine import views

app_name = 'mine'
urlpatterns = [

    path("mine/", views.mine),
    path("changemineinfo/", views.change_mine_info),
    path("changepassword/", views.change_password),
    path("changepassword/", views.change_password),
    path("sendcode/", views.send_code),
    path("msg_login/", views.msg_login),
]
