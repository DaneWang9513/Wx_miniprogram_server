from django.http import HttpResponse
from .models import kaoqin
import json
import datetime
import datetime
import requests
import urllib
import sys
import simplejson
#import pymssql
import pymysql
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

def getKaoqin(request):
    data = json.loads(request.body)
    username = data['username']
    xiaofei_list = []
    #nian_yue=str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)
    nian_yue = str(datetime.datetime.now().year) + '-' + '0'+str(datetime.datetime.now().month)
    print(nian_yue)
    name = kaoqin.objects.all().filter(username=username,kq_sj__contains=nian_yue).order_by('-kq_sj').distinct()
    print(name.query)
    for it in name:
        #order = []
        #order_result = kaoqin.objects.all().filter(id = it['id'])
        #for item in order_result:
            #order.append({'Cash_amt':item.Cash_amt,'Sub_amt':item.Sub_amt})
        xiaofei_list.append({'kq_sj':it.kq_sj})
    return HttpResponse(json.dumps(xiaofei_list,cls=CJsonEncoder))

def createKaoqin(request):
    data = json.loads(request.body)
    print(data)

    topic = data['topic']#时长
    #topic = str(topic)
    topic = int(topic)
    startTime = data['startTime']
    endTime = data['endTime']
    kq_type = data['kq_type']#考勤类型
    #topic = data['topic']
    content = data['content']
    user_name = data['user_name']
    oa_id = data['oa_id']
    dept_id = data['dept_id']
    kq_typeid=''
    kq_tp = ''
    corpid = 'wx583f1ddac65b448c'
    corpsecret = 'ee06fda6c9485137f9edbff05a4e0cf8'
    #accesstoken = gettoken(corpid, corpsecret)
    accesstoken = get_token()
    code1 = senddata(accesstoken, topic)
    code2 = senddata(accesstoken, content)
    if(kq_type=='1'):
        kq_tp='加班'
        kq_typeid='JB'
    elif(kq_type=='2'):
        kq_tp='公假'
        kq_typeid='A'
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if (code1 == 0 and code2 == 0):
            db = pymysql.connect(host="124.205.74.195", user="root",
                                 password="myoa888", db="TD_OA", port=3336)
            # 使用cursor()方法获取操作游标
            cur = db.cursor()
            sql_insert = "insert into attend_event(USER_ID,USER_NAME,DEPT_ID,EVENT_TYPE,EVENT_DATE1,EVENT_DATE2,ANNUAL_LEAVE,TIME_LENGTH,TIME_TYPE,TIME_UNIT,REASON,RECORD_TIME,RECORD_ID,STATUS,AUDIT_TIME) values ('%s','%s','%s','%s','%s','%s',%d,%d,'%s',%d,'%s','%s','%s',%d,'%s')"
            try:
                cur.execute(sql_insert % (oa_id, user_name, dept_id, kq_tp, startTime, endTime, 0.0,topic,kq_typeid,1,content,now_time,oa_id,0,'0000-00-00 00:00:00'))  # 像sql语句传递参数
                # 提交
                db.commit()
                print("success")
                tmp = ['True']
            except Exception as e:
                # 错误回滚
                db.rollback()
            finally:
                db.close()  # 关闭连接
    else:
        tmp = ['违法内容']

    #tmp = ['True']
    return HttpResponse(tmp)
    
def hKaoqin(request):
    data = json.loads(request.body)
    username = data['username']
    nian_yue = data['nian_yue']
    xiaofei_list = []
    #nian_yue=str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)
    #nian_yue = str(datetime.datetime.now().year) + '-' + '0'+str(datetime.datetime.now().month)
    print(nian_yue)
    name = kaoqin.objects.all().filter(username=username,kq_sj__contains=nian_yue).order_by('-kq_sj').distinct()
    print(name.query)
    for it in name:
        #order = []
        #order_result = kaoqin.objects.all().filter(id = it['id'])
        #for item in order_result:
            #order.append({'Cash_amt':item.Cash_amt,'Sub_amt':item.Sub_amt})
        xiaofei_list.append({'kq_sj':it.kq_sj})
    return HttpResponse(json.dumps(xiaofei_list,cls=CJsonEncoder))

