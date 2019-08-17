from django.urls import path

from find1 import views

app_name = 'find1'
urlpatterns = [

    path("menutypelist/", views.menutype_list),
    path("menulist/", views.menu_list),
    path("baikelist/", views.baike_list),
]
