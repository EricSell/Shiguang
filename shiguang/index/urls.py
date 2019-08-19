from django.urls import path, re_path

from index import views

app_name = 'index'
urlpatterns = [

    path("register/", views.register),
    path("login/", views.login),
    path("logout/", views.logout),
    path("login_send_email/", views.login_send_email),
    path("login_mail_captcha/", views.login_mail_captcha),
    re_path(r"^menulist/$", views.Menu_list),
    re_path(r"^menudetails/$", views.Menu_details),

    re_path(r"^clecklive/$", views.cleck_live),
    re_path(r"^cleckcollect/$", views.cleck_collect),
]
