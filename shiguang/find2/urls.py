from django.urls import path

from find2 import views
app_name = 'find2'
urlpatterns = [
    path("baikelist/", views.baike_list, name='baike_list')
]