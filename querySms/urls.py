from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'sms_tixing',views.sms_tixing),
]