from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'getTaolun',views.getTaolun),
    url(r'Taolun_detail',views.Taolun_detail)
]