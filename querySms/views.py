from django.shortcuts import render
from django.http import HttpResponse
from .models import sms
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
import pymysql
# Create your views here.

# Create your views here.
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

def sms_tixing(request):
    data = json.loads(request.body)
    #FormerID = data['FormerID']
    #signin_list = []
    to_id=str(data['to_id'])
    sms_list = []
    conn = pymysql.connect(host="172.16.125.48", user="root", password="myoa888", db="TD_OA", port=3336)
    cursor = conn.cursor()
    sql = "SELECT sms.REMIND_FLAG,sms_body.CONTENT,sms.REMIND_TIME FROM sms,sms_body where sms.BODY_ID=sms_body.BODY_ID AND sms.REMIND_FLAG!=0 AND TO_ID= %s ORDER BY sms.SMS_ID DESC" % (to_id)
    try:
        cursor.execute(sql)  # 执行sql语句

        results = cursor.fetchall()  # 获取查询的所有记录
        for row in results:
            flag = row[0]
            cont = row[1]
            time = row[2]
            re_time = datetime.datetime.fromtimestamp(time)
            re_time = re_time.strftime("%Y-%m-%d %H:%M:%S")
            sms_list.append({'remind_flag': '未处理', 'body': cont, 'remind_time': re_time})
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()  # 关闭连接
    tmp = json.dumps(sms_list,cls=CJsonEncoder)
    return HttpResponse(tmp)
