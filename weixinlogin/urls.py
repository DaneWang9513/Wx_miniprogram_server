from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'weixinlogin', views.weixinlogin),
    url(r'deptUser', views.deptUser),
    url(r'changePassword', views.changePassword),
    url(r'huoquid', views.huoquid),
]