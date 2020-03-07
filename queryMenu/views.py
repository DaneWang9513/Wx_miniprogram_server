from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import menu as Menu
from order.models import Order
from django.db.models import Sum
import json
import datetime
# Create your views here.

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

def queryMenu(request):
    # menu = [{'typeName': '快餐类','''menuContent':[{'name':'炸鸡'},{'name':'鸡腿'}]},{}]
    data = json.loads(request.body)
    username = data['username']
    menu = []
    typeName = []
    feed_list = []
    feed = []
    typeName = Menu.objects.all().values('typeName').order_by('typeName').distinct()
    for it in typeName:
        my_dict = {}
        my_dict['typeName'] = it['typeName']
        menuContent = Menu.objects.filter(typeName=it['typeName'],status='上架')
        list = []
        for item in menuContent:
            today = datetime.datetime.today()
            print(today)
            if(item.jz_date_time>today):
                list.append({'typeName':item.typeName,'name':item.name,'src':str(item.src),'sales':item.sales,'rating':round(item.rating,1),'numb':0, 'price':item.price,'xiaoliang':item.xiaoliang,'jz_date_time':item.jz_date_time,'lq_date_time':item.lq_date_time,'jz_status':0,'sales_fz':item.sales_fz})
            else:
                list.append({'typeName': item.typeName, 'name': item.name, 'src': str(item.src), 'sales': item.sales,
                             'rating': round(item.rating, 1), 'numb': 0, 'price': item.price,'xiaoliang': item.xiaoliang,
                             'jz_date_time': item.jz_date_time,'lq_date_time':item.lq_date_time, 'jz_status': 1,'sales_fz':item.sales_fz})
        my_dict['menuContent'] = list
        if len(list) != 0:
            menu.append(my_dict)
    tmp = json.dumps(menu,cls=CJsonEncoder)
    return HttpResponse(tmp)