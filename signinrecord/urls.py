from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'RecordSignin',views.RecordSignin),
    url(r'Detail',views.Detail),
    url(r'SearchPatic',views.SearchPatic)
]