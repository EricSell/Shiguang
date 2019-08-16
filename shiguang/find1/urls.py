from django.urls import path

from find1 import views
app_name = 'find1'
urlpatterns = [

    path("index/", views.index)
]