from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'getXiaofei', views.getXiaofei),
    url(r'getYue', views.getYue),
    url(r'aXiaofei', views.aXiaofei)
]