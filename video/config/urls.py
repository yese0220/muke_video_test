#coding: utf-8
from django.contrib import admin
from django.urls import path,include
from app.dashboard import urls as dashboard_urls
from app.client import urls as client_urls

urlpatterns = [
    #我们不使用默认的admin，所以可以直接去掉
    #path('admin/', admin.site.urls),
    path('dashboard/',include(dashboard_urls)),
    path('client/',include(client_urls))
]
