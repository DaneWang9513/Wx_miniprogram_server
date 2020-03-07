from django.shortcuts import render
from django.http import HttpResponse
from .models import news
from signinrecord.models import SigninRecord as SigninRecord
#from launchsignin.models import Signin as Signin
#from launchsignin.models import SigninRecord as SigninRecord
import json
import datetime
import json
import os
import datetime
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

def getNews(request):
    data = json.loads(request.body)
    #FormerID = data['FormerID']
    #signin_list = []
    to_id=str(data['to_id'])
    news_list = []
    name = news.objects.all().filter(to_id=to_id).order_by('-news_time').distinct()[0:60]
    print(name.query)
    for item in name:
        news_list.append({'id':item.id,'subject':item.subject,'content':item.content,'provider':item.provider,'news_time':item.news_time,'keyword':item.keyword})
    tmp = json.dumps(news_list,cls=CJsonEncoder)
    return HttpResponse(tmp)

def News_detail(request):
    data = json.loads(request.body)
    id = data['id']
    news_d_list = []
    name = news.objects.all().filter(id=id)
    print(name.query)
    for item in name:
        news_d_list.append({'subject':item.subject,'content':item.content,'provider':item.provider,'news_time':item.news_time})
    tmp = json.dumps(news_d_list,cls=CJsonEncoder)
    return HttpResponse(tmp)