from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.contrib.auth.hashers import make_password, check_password
from weixinlogin.models import UserProfile
from suds.client import Client
from zeep import Client as ZClient
import xmltodict
import datetime

# Create your views here.

def weixinlogin(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    openid = data['openid']
    #dept = data['dept']
    user = UserProfile.objects.filter(username=username)[0]
    dept = user.dept
    user_oa_id = user.user_oa_id
    first_name = user.first_name
    dept_id = user.dept_id
    is_mes = user.is_mes
    is_smzc = user.is_saomazc
    is_grzc = user.is_gerenzc
    is_bmzc = user.is_bumenzc
    mes_id = user.user_mes_id
    mes_dept = user.user_mes_dept
    is_gzcx = user.is_gerengz
    user.openid =openid
    user.save()
    print(check_password(password,user.password))
    print(dept)
    if check_password(password,user.password):
        ret = 'True&'+dept+'&'+first_name+'&'+user_oa_id+'&'+dept_id+'&'+is_mes+'&'+is_smzc+'&'+is_grzc+'&'+is_bmzc+'&'+mes_id+'&'+mes_dept+'&'+is_gzcx
    else:
        ret = 'mlgb'
    #print(json.dumps(ret,dept))
    return HttpResponse(json.dumps(ret))
    
def deptUser(request):
    data = json.loads(request.body)
    dept = data['dept']
    dept_list = []
    user = UserProfile.objects.all().filter(dept=dept).values('first_name','mobile_no','tel_no_dept').order_by('paixu_id').distinct()
    for it in user:
        dept_list.append({'first_name': it['first_name'], 'mobile_no': it['mobile_no'],'tel_no_dept':str(it['tel_no_dept'])})
    print(dept_list)
    return HttpResponse(json.dumps(dept_list))

def changePassword(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user = UserProfile.objects.filter(username=username)[0]
    user.password = make_password(password)
    user.save()
    ret = 'True'
    return HttpResponse(json.dumps(ret))

def huoquid(request):
    if request.method == 'GET':
        rescode = request.GET.get('code')
    #if (request.method == 'POST'):
        #postBody = request.body
        #print(postBody)
    #data = json.loads(postBody)
    #rescode = data['code']
    print(rescode)
    url = "https://api.weixin.qq.com/sns/jscode2session"
    params = {"appid":"wx583f1ddac65b448c",
              "secret":"ee06fda6c9485137f9edbff05a4e0cf8",
              "js_code":rescode,
              "grant_type":"authorization_code"}

    ret = requests.get(url=url,params=params).json().get("openid")
    print("openid:" + ret)
    return HttpResponse(json.dumps(ret))
    #password = data['password']

'''    
def gSalary(request):
    if request.method == 'GET':
        periodtime = request.GET.get('periodtime')
        userno = request.GET.get('userno')
    print(periodtime,userno)
    url = 'http://172.16.125.52:8098/ExtechWEB/ExtechAXInterfaceService.asmx?wsdl'
    client = Client(url)
    xml_result = client.service.findWageLine(periodtime,userno)
    # 先将xml转换为字典
    data = xmltodict.parse(xml_result)
    data1 = data["NewDataSet"]["TSC_HR_TWageLine"]
    # 再将字典转换为json
    strjson = json.dumps(data1)
    return HttpResponse(strjson)
'''