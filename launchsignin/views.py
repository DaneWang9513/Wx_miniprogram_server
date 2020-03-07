from django.shortcuts import render
from django.http import HttpResponse
from .models import Signin
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
from django.contrib.auth.hashers import make_password, check_password
from weixinlogin.models import UserProfile

# Create your views here.
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

#POST请求业务接口
def run(method,url,data):
        headers = {
                'content-type':'application/json',
                'Authorization':'Basic aGVhbHRoY2hlY2tAaW50ZWxsaWNyZWRpdC5jbjpqZXJyeTM5OlBASGVhbHRoY2hlY2s='
        }
        if method == 'POST':
                data_json = json.dumps(data)
                start_time = datetime.datetime.now()
                raw = requests.post(url,data_json,headers=headers)
                end_time = datetime.datetime.now()
                Rtime=(end_time-start_time).microseconds / 1000
                status = raw.status_code
                subject = '%s status:\t%s\n%s 时延:%s' %(url,status,url,Rtime)
                return subject
#获取access_token
def gettoken(corpid,corpsecret):
    gettoken_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+corpid +'&secret='+corpsecret
    print(gettoken_url)
    try:
        token_file = urllib.request.urlopen(gettoken_url)
    except urllib.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token

def get_token():
    try:
        with open("E:/backend/access_token.txt", "r") as f:
            content = f.read()
            print(content)
            data_dict = eval(content)
            time = datetime.datetime.strptime(data_dict["time"], '%Y-%m-%d %H:%M:%S')

        if (datetime.datetime.now() - time).seconds < 7000:
            print("未到两小时，从文件读取")
            return data_dict["access_token"]
        else:
            # 超过两小时，重新获取
            print("超过两小时，重新获取")
            payload = {
                'grant_type': 'client_credential',
                'appid': '',  # 公众号appid,按自己实际填写
                'secret': '',
            }
            url = "https://api.weixin.qq.com/cgi-bin/token?"

            try:
                respone = requests.get(url, params=payload, timeout=50)
                access_token = respone.json().get("access_token")
                content = "{'access_token':'" + str(access_token) + "','time':'" + str(
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "'}"
                # 写入文件
                with open("E:/backend/access_token.txt", "w") as f:
                    f.write(content)

                print("get_token", access_token)
                return access_token
            except Exception as e:
                print(e)
    except Exception as e:
        print("get_token,file", e)


def senddata(access_token,subject):
    send_url = 'https://api.weixin.qq.com/wxa/msg_sec_check?access_token=' + access_token
    send_values = {
         "content":subject
        }
#    send_data = json.dumps(send_values, ensure_ascii=False)
    send_data = simplejson.dumps(send_values, ensure_ascii=False).encode('utf-8')
    send_request = urllib.request.Request(send_url, send_data)
    response = json.loads(urllib.request.urlopen(send_request).read())
    print(str(response))
    return response['errcode']


def commitSignin(request):
    data = json.loads(request.body)
    #print(data)
    FormID = data['FormID']
    startTime = data['startTime']
    endTime = data['endTime']
    FormerID = data['FormerID']
    topic = data['topic']
    content = data['content']
    corpid = 'wx583f1ddac65b448c'
    corpsecret = 'ee06fda6c9485137f9edbff05a4e0cf8'
    #accesstoken = gettoken(corpid, corpsecret)
    accesstoken = get_token()
    code1 = senddata(accesstoken, topic)
    code2 = senddata(accesstoken, content)
    if(code1==0 and code2==0):
        Signin.objects.create(FormID=FormID,startTime=startTime,endTime=endTime,FormerID=FormerID,topic=topic,content=content)
        tmp = ['True']
    else:
        tmp = ['违法内容']
    return HttpResponse(tmp)


def getSignin(request):
    data = json.loads(request.body)
    FormerID = data['FormerID']
    signin_list = []
    name = Signin.objects.all().filter(FormerID=FormerID)
    print(name.query)
    for item in name:
        signin_list.append({'FormID':item.FormID,'startTime':item.startTime,'endTime':item.endTime,'FormerID':item.FormerID,'topic':item.topic,'content':item.content})
    tmp = json.dumps(signin_list)
    return HttpResponse(tmp)

def deleteSignin(request):
    data = json.loads(request.body)
    FormID = data['FormID']
    Signin.objects.filter(FormID=FormID).delete()
    SigninRecord.objects.filter(FormID=FormID).delete()
    tmp = ['True']
    return HttpResponse(tmp)

