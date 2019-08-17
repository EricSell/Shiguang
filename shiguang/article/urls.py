from django.urls import path

from article import views

app_name = 'article'
urlpatterns = [

    path("article_list/", views.article_list),
    path("article_detail/", views.article_detail),
]
