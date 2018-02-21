"""MiniWeiboSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from app01 import views
from django.conf.urls import url
from django.views.generic.base import RedirectView

handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.page_error


urlpatterns = [
    url(r'^$',views.homepage),
    url(r'^favicon.ico$',RedirectView.as_view(url='/static/img/about_UI/favicon.ico')),
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('login/',views.login),
    path('register/',views.register),
    path('send_code/',views.send_code),
    path('check_img_code/',views.check_img_code),
    path('messageShow/',views.messageShow),
]
