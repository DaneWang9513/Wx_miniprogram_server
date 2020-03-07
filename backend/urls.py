"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf.global_settings import MEDIA_ROOT
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from backend import settings

urlpatterns = [
    url(r'^static/(?P<path>.*)$',serve,{'document_root': settings.STATIC_ROOT,}),
    url(r'^', admin.site.urls),
    url(r'^', include('queryCaidan.urls')),
    url(r'^', include('queryMenu.urls')),
    url(r'^', include('queryXiaofei.urls')),
    url(r'^', include('order.urls')),
    url(r'^',include('weixinlogin.urls')),
    url(r'^',include('launchsignin.urls')),
    url(r'^',include('signinrecord.urls')),
    url(r'^',include('queryNews.urls')),
    url(r'^',include('queryNotify.urls')),
    url(r'^',include('queryKq.urls')),
    url(r'^',include('queryTaolun.urls')),
    url(r'^',include('querySms.urls')),
    #re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    #url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,'show_indexes':True}),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)