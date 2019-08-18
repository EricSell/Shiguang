from django.urls import path

from index import views

app_name = 'index'
urlpatterns = [

    path("register/", views.register),
    path("login/", views.login),
    path("logout/", views.logout),
]
