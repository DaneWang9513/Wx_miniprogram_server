from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'commitSignin',views.commitSignin),
    url(r'getSignin',views.getSignin),
    url(r'deleteSignin',views.deleteSignin)
]