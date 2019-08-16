from django.urls import path

from mine import views
app_name = 'mine'
urlpatterns = [

    path("index/", views.index)
]
