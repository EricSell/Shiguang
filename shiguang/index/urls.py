from django.urls import path

from index import views

app_name = 'index'
urlpatterns = [

    path("register/", views.register),
    path("login/", views.login),
    path("logout/", views.logout),
    path("login_send_email/", views.login_send_email),
    path("login_mail_captcha/", views.login_mail_captcha),
]
