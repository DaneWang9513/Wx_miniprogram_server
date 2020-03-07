from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'getNotifys',views.getNotifys),
    url(r'Notifys_detail',views.Notifys_detail)
]