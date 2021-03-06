from django.urls import path

from find2 import views
app_name = 'find2'
urlpatterns = [
    # path("baikelist/", views.baike_list, name='baike_list'),
    path("baikedetail/", views.baike_detail, name='baike_detail'),
    path("baikedetaillove/", views.baike_detail_love, name='baike_detail_love'),
    path("baikedetailcollect/", views.baike_detail_collect, name='baike_detail_collect'),
    path("userlist/", views.user_list, name='userlist'),
    path("userdetail/", views.user_detail, name='userdetail'),
    path("userdetailfollow/", views.user_detail_follow, name='userdetailfollow'),
]