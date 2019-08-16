from django.urls import path

from find2 import views
app_name = 'find2'
urlpatterns = [

    path("index/", views.index)
]