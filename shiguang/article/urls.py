from django.urls import path

from index import views

app_name = 'article'
urlpatterns = [

    path("index/", views.index)
]
