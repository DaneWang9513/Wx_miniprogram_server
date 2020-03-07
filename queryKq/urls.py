from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'getKaoqin', views.getKaoqin),
    url(r'createKaoqin', views.createKaoqin),
    url(r'hKaoqin', views.hKaoqin)
    #url(r'getDengji', views.getDengji),

    #url(r'getYue', views.getYue),
]