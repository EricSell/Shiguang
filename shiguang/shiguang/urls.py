"""shiguang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from shiguang import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path("index/", include("index.urls", namespace="index")),
    path("find1/", include("find1.urls", namespace="find1")),
    path("find2/", include("find2.urls", namespace="find2")),
    path("article/", include("article.urls", namespace="article")),
    path("mine/", include("mine.urls", namespace="mine")),
]

# 部署的时候收集静态文件
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
