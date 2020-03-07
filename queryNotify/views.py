from django.shortcuts import render
from django.http import HttpResponse
from .models import notifys
from signinrecord.models import SigninRecord as SigninRecord
#from launchsignin.models import Signin as Signin
#from launchsignin.models import SigninRecord as SigninRecord
import json
import datetime
import json
import os
import datetime
import time
import requests
import urllib
import sys
import simplejson

# Create your views here.
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

def getNotifys(request):
    data = json.loads(request.body)
    #FormerID = data['FormerID']
    #signin_list = []
    to_id=str(data['to_id'])
    news_list = []
    t = time.time()
    t = int(t)
    name = notifys.objects.all().filter(to_id=to_id).order_by('-send_time').distinct()[0:60]
    print(name.query)
    for item in name:
        if(item.end_date>=t or item.end_date==0):
            news_list.append({'id':item.id,'subject':item.subject,'content':item.content,'from_name':item.from_name,'send_time':item.send_time,'keyword':item.keyword})
    tmp = json.dumps(news_list,cls=CJsonEncoder)
    return HttpResponse(tmp)

def Notifys_detail(request):
    data = json.loads(request.body)
    id = data['id']
    news_d_list = []
    name = notifys.objects.all().filter(id=id)
    print(name.query)
    for item in name:
        news_d_list.append({'subject':item.subject,'content':item.content,'from_name':item.from_name,'send_time':item.send_time})
    tmp = json.dumps(news_d_list,cls=CJsonEncoder)
    return HttpResponse(tmp)