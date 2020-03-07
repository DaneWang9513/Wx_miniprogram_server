from django.shortcuts import render
from django.http import HttpResponse
from .models import SigninRecord
from launchsignin.models import Signin as Signin
#from launchsignin.models import Signin as Signin
#from launchsignin.models import SigninRecord as SigninRecord
import json
import datetime
import time
from django.contrib.auth.hashers import make_password, check_password
from weixinlogin.models import UserProfile

# Create your views here.
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)


def RecordSignin(request):
    data = json.loads(request.body)
    #print(data['FormID'])
    FormID = data['FormID']
    studentID = data['studentID']
    studentName = data['studentName']
    #FormerID = data['FormerID']
    topic = data['topic']
    endTime = Signin.objects.all().filter(FormID=FormID).values('endTime').distinct()[0]
    print(endTime['endTime'])
    d1 = endTime['endTime']
    d2 = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
    if(d2<=d1):
    #content = data['content']
        SigninRecord.objects.create(FormID=FormID,studentID=studentID,studentName=studentName,topic=topic)
        tmp = ['True']
    else:
        tmp = ['False']
    return HttpResponse(tmp)

def Detail(request):
    data = json.loads(request.body)
    FormID = data['FormID']
    signin_list = []
    name = SigninRecord.objects.all().filter(FormID=FormID)
    print(name.query)
    for item in name:
        signin_list.append({'FormID':item.FormID,'studentID':item.studentID,'studentName':item.studentName,'topic':item.topic})
    tmp = json.dumps(signin_list)
    return HttpResponse(tmp)

def SearchPatic(request):
    data = json.loads(request.body)
    studentID = data['studentID']
    studentName = data['studentName']
    patic_list = []
    detail = SigninRecord.objects.all().filter(studentID=studentID,studentName=studentName).distinct()
    print(detail.query)
    for item in detail:
        #patic_list.append(
            #{'FormID': item.FormID, 'studentID': item.studentID, 'studentName': item.studentName, 'topic': item.topic})
        patic_list.append(item.FormID)

    result_list = []
    for each in patic_list:
        result = Signin.objects.filter(FormID=each)
        for item in result:
            result_list.append({'FormID':item.FormID,'startTime':item.startTime,'endTime':item.endTime,'FormerID':item.FormerID,'topic':item.topic,'content':item.content})

    print(result_list)
    tmp = json.dumps(result_list)
    return HttpResponse(tmp)

