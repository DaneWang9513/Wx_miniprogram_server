from django.http import HttpResponse
from .models import xiaofei
import json
import datetime
from django.contrib.auth.hashers import make_password, check_password
from weixinlogin.models import UserProfile

# Create your views here.
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

def getXiaofei(request):
    data = json.loads(request.body)
    username = data['username']
    xiaofei_list = []
    #nian_yue = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month)
    nian_yue = str(datetime.datetime.now().year) + '-' + '0'+str(datetime.datetime.now().month)
    print(nian_yue)
    yue_fen = str(datetime.datetime.now().month)
    name = xiaofei.objects.all().filter(username=username,wacc_sj__contains=nian_yue).values('id','username').order_by('-wacc_sj').distinct()
    print(name.query)
    for it in name:
        order = []
        order_result = xiaofei.objects.all().filter(id = it['id'])
        for item in order_result:
            order.append({'Cash_amt':str(item.Cash_amt),'Sub_amt':str(item.Sub_amt)})
        xiaofei_list.append({'order':order,'wacc_sj':item.wacc_sj})
    return HttpResponse(json.dumps(xiaofei_list,cls=CJsonEncoder))

def getYue(request):
    data = json.loads(request.body)
    username = data['username']
    yue_list = []
    name = xiaofei.objects.all().filter(username=username).values('id','username').order_by('-wacc_sj').distinct()[0:1]
    print(name.query)
    for it in name:
        yue = []
        yue_result = xiaofei.objects.all().filter(id = it['id'])
        for item in yue_result:
            yue.append({'New_card_cash':str(item.New_card_cash),'New_card_subsidy':str(item.New_card_subsidy)})
        yue_list.append({'New_card_cash':str(item.New_card_cash),'New_card_subsidy':str(item.New_card_subsidy)})
    return HttpResponse(json.dumps(yue_list,cls=CJsonEncoder))

def aXiaofei(request):
    data = json.loads(request.body)
    username = data['username']
    nian_yue = data['nian_yue']
    xiaofei_list = []
    #nian_yue = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month)
    #nian_yue = str(datetime.datetime.now().year) + '-' + '0'+str(datetime.datetime.now().month)
    print(nian_yue)
    yue_fen = str(datetime.datetime.now().month)
    name = xiaofei.objects.all().filter(username=username,wacc_sj__contains=nian_yue).values('id','username').order_by('-wacc_sj').distinct()
    print(name.query)
    for it in name:
        order = []
        order_result = xiaofei.objects.all().filter(id = it['id'])
        for item in order_result:
            order.append({'Cash_amt':str(item.Cash_amt),'Sub_amt':str(item.Sub_amt)})
        print(order)
        xiaofei_list.append({'order':order,'wacc_sj':item.wacc_sj})
    return HttpResponse(json.dumps(xiaofei_list,cls=CJsonEncoder))