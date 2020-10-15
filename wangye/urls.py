"""wangye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path

from mysql02 import views
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"add/", views.addbook),
    # path(r"login/", views.login),
    path(r"2/", views.manhua),
    path(r"index.html", views.index),
    path(r"search.html", views.search),
    path(r"other-features.html", views.about),
    path(r"blog-3-column.html", views.blog),

    path(r"in1.html", views.about1),
    path(r"in2.html", views.about2),
    path(r"in3.html", views.about3),
    path(r"in4.html", views.about4),
    path(r"in5.html", views.about5),
    path(r"in6.html", views.about6),
    path(r"in7.html", views.about7),

    url(r'^1/(?P<path>.*)$', serve, {'document_root': 'C:/bd/scrapy/wangye/1'})
    # (\d+)用于匹配获取表记录的主键（书的id）
    # re_path(r"books/(\d+)/delete", views.bookdel),
    # re_path(r"books/(\d+)/edit", views.bookedit)

]
