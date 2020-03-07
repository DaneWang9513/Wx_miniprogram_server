from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'getOrder', views.getOrder),
    url(r'commitOrder',views.commitOrder),
    url(r'postComment',views.postComment),
    url(r'tongjiOrder',views.tongjiOrder),
    url(r'countOrder',views.countOrder),
    url(r'nianyueOrder',views.nianyueOrder)
]