from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'getNews',views.getNews),
    url(r'News_detail',views.News_detail)
]