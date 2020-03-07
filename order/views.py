from django.shortcuts import render
from django.http import HttpResponse
from .models import Order,TodayOrder
from queryMenu.models import menu as Menu
import json
import datetime
from django.contrib.auth.hashers import make_password, check_password
from weixinlogin.models import UserProfile
from order_tj.models import Order_tj as Order_tj

# Create your views here.
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)


def update_num(lq_date_time,name,num):
    food = Menu.objects.filter(name=name,lq_date_time=lq_date_time).order_by('-id')[0]
    #number = min(max(food.sales, 200), 2000)
    food.sales += num
    food.xiaoliang -= num
    food.save()
    
def update_num_tj(lq_date_time,dept,num,food_name):
    tj_item = Order_tj.objects.filter(lq_date_time=lq_date_time,dept=dept).order_by('-id')[0]
    #number = min(max(food.sales, 200), 2000)
    if (("盒饭1" in food_name) == True):
        # print('增加数量:'+number_hf)
        tj_item.number_h1 -= num
        tj_item.save()
    else:
        tj_item.number_h2 -= num
        tj_item.save()


def postComment(request):
    data = json.loads(request.body)['order']
    print(data)
    order_id = data['order_id'] + '='
    order = Order.objects.filter(order_id=order_id)
    for it in data['order']:
        for item in order:
            if it['name'] == item.food_name:
                item.numb = it['numb']
                update_num(it['lq_date_time'],it['name'], it['numb'])
                update_num_tj(it['lq_date_time'],item.dept, it['numb'],it['name'])
                item.save();
    Order.objects.filter(order_id=order_id).delete()
    '''
    for it in data['order']:
        for item in order:
            if it['name'] == item.food_name:
                item.score = it['score']
                update_score(it['name'],it['score'])
                item.state = data['state']
                item.comment = data['comment']
                item.save();
    '''
    tmp = ['True']
    return HttpResponse(tmp)


def commitOrder(request):
    data = json.loads(request.body)
    username = data['username']
    dept = data['dept']
    first_name = data['first_name']
    date_time = data['date']
    usercost = data['cost']

    state = data['state']
    comment = data['comment']
    order_list = data['order']
    for item in order_list:
        typeName = item['typeName']
        food_name = item['name']
        number = item['numb']
        lq_time = item['lq_time']
        #print(lq_time)
        order_id = make_password(username + date_time)
        food = Menu.objects.filter(name=food_name,lq_date_time=lq_time).order_by('-id')[0]
        jz_date_time=food.jz_date_time
        food.sales -= number
        food.xiaoliang += number
        #print(float(food.xiaoliang/food.sales_fz)*100)
        if(food.xiaoliang>=food.sales_fz):
            food.fh_status='符合'
        food.save()
        cost = food.price * number
        Order.objects.create(username=username,dept=dept,first_name=first_name,order_id=order_id,food_name=food_name,comment=comment,score=5,date_time=date_time,number=number,state=state,cost=cost,typeName=typeName,jz_date_time=jz_date_time,lq_date_time=food.lq_date_time)
        result = Order_tj.objects.filter(lq_date_time=food.lq_date_time,dept=dept)
        if (result.count()!=0):
            lq_date_time_hf = food.lq_date_time
            dept_item = Order_tj.objects.filter(lq_date_time=lq_date_time_hf,dept=dept)[0]
            print("盒饭1" in food_name)
            number_hf = number
            if(("盒饭1" in food_name) == True):
                #print('增加数量:'+number_hf)
                dept_item.number_h1 += number_hf
                dept_item.save()
            else:
                dept_item.number_h2 += number_hf
                dept_item.save()
        else:
            number_hf = number
            lq_date_time_hf = food.lq_date_time
            if (("盒饭1" in food_name)==True):
                Order_tj.objects.create(lq_date_time=lq_date_time_hf,dept=dept,number_h1=number_hf)
            else:
                Order_tj.objects.create(lq_date_time=lq_date_time_hf,dept=dept,number_h2=number_hf)
        ReTodayOrder(food_name,number,state,date_time)
    add_usercost(username,usercost)
    tmp = ['True']
    return HttpResponse(tmp)


def add_usercost(username,cost):
    src_cost = UserProfile.objects.filter(username=username)[0]
    src_cost.cost += cost
    src_cost.save()


def ReTodayOrder(food_name,number,state,date_time):
    today = datetime.date.today()
    tomorrow = datetime.date(today.year,today.month,today.day+1)
    order_list = TodayOrder.objects.filter(date_time__range=(today,tomorrow))
    order = order_list.filter(food_name=food_name)
    if(len(order)):
        for item in order:
            item.number += number
            item.date_time = date_time
            item.save()
    else:
        TodayOrder.objects.create(food_name=food_name,number=number,state=state,date_time=date_time)


def get_src(lq_date_time,name):
    result = Menu.objects.filter(name=name,lq_date_time=lq_date_time).values('src').order_by('-id')[0]
    print("src:"+result['src'])
    if result:
        return str(result['src'])
    else:
        return ''


def getOrder(request):
    data = json.loads(request.body)
    username = data['username']
    order_list = []
    name = Order.objects.all().filter(username=username).values('order_id','username').order_by('-date_time').distinct()[0:60]
    print(name.query)
    for it in name:
        order = []
        order_result = Order.objects.all().filter(order_id = it['order_id'])
        today = datetime.datetime.today()
        print(today)
        for item in order_result:
            if (item.jz_date_time > today):
                food = Menu.objects.filter(name=item.food_name,lq_date_time=item.lq_date_time).order_by('-id')[0]
                print("name:"+food.name)
                order.append({'name':item.food_name,'numb':item.number,'typeName':item.typeName,'score':item.score,'src':get_src(item.lq_date_time,item.food_name),'jz_status':0,'fh_status':0,'lq_date_time':item.lq_date_time})
                #print("order:"+order)
            else:
                food = Menu.objects.filter(name=item.food_name,lq_date_time=item.lq_date_time).order_by('-id')[0]
                print(food.name)
                order.append(
                    {'name': item.food_name, 'numb': item.number, 'typeName': item.typeName, 'score': item.score,
                     'src': get_src(item.lq_date_time,item.food_name), 'jz_status': 1,'fh_status':food.fh_status,'lq_date_time':item.lq_date_time})
                #print("order:" + order)
        if (item.jz_date_time > today):
            order_list.append({'order':order,'comment':item.comment,'date':item.date_time,'state':item.state,'order_id':item.order_id[:-1],'jz_status':0,'lq_date_time':item.lq_date_time})
        else:
            #if()
            order_list.append({'order': order, 'comment': item.comment, 'date': item.date_time, 'state': item.state,
                               'order_id': item.order_id[:-1], 'jz_status': 1,'lq_date_time':item.lq_date_time})
    return HttpResponse(json.dumps(order_list,cls=CJsonEncoder))
    
def nianyueOrder(request):
    data = json.loads(request.body)
    username = data['username']
    nian_yue = data['nian_yue']
    order_list = []
    name = Order.objects.all().filter(username=username, date_time__contains=nian_yue).values('order_id','username').order_by('-date_time').distinct()[0:60]
    print(name.query)
    for it in name:
        order = []
        order_result = Order.objects.all().filter(order_id = it['order_id'])
        today = datetime.datetime.today()
        print(today)
        for item in order_result:
            if (item.jz_date_time > today):
                food = Menu.objects.filter(name=item.food_name,lq_date_time=item.lq_date_time).order_by('-id')[0]
                print("name:"+food.name)
                order.append({'name':item.food_name,'numb':item.number,'typeName':item.typeName,'score':item.score,'src':get_src(item.lq_date_time,item.food_name),'jz_status':0,'fh_status':0,'lq_date_time':item.lq_date_time})
                #print("order:"+order)
            else:
                food = Menu.objects.filter(name=item.food_name,lq_date_time=item.lq_date_time).order_by('-id')[0]
                print(food.name)
                order.append(
                    {'name': item.food_name, 'numb': item.number, 'typeName': item.typeName, 'score': item.score,
                     'src': get_src(item.lq_date_time,item.food_name), 'jz_status': 1,'fh_status':food.fh_status,'lq_date_time':item.lq_date_time})
                #print("order:" + order)
        if (item.jz_date_time > today):
            order_list.append({'order':order,'comment':item.comment,'date':item.date_time,'state':item.state,'order_id':item.order_id[:-1],'jz_status':0,'lq_date_time':item.lq_date_time})
        else:
            #if()
            order_list.append({'order': order, 'comment': item.comment, 'date': item.date_time, 'state': item.state,
                               'order_id': item.order_id[:-1], 'jz_status': 1,'lq_date_time':item.lq_date_time})
    return HttpResponse(json.dumps(order_list,cls=CJsonEncoder))
    
def tongjiOrder(request):
    data = json.loads(request.body)
    dept = data['dept']
    nian_yue = data['nian_yue']
    tongji_list = []
    yue_fen = str(datetime.datetime.now().month)
    name = Order.objects.all().filter(dept=dept, lq_date_time__contains=nian_yue).values('first_name','food_name','number').order_by('-date_time').distinct()
    print(name)
    for it in name:
        #order = []
        #order_result = Order.objects.all().filter(id=it['id'])
        #or item in order_result:
            #order.append({'first_name': str(item.first_name), 'food_name': str(item.food_name),'number':str(item.number)})
        #print(order)
        tongji_list.append({'first_name': it['first_name'], 'food_name': it['food_name'],'number':str(it['number'])})
    print(tongji_list)
    return HttpResponse(json.dumps(tongji_list, cls=CJsonEncoder))
    
def countOrder(request):
    data = json.loads(request.body)
    #username = data['username']
    dept = data['dept']
    nian_yue = data['nian_yue']
    shuliang_list = []
    number_h1=0
    number_h2=0
    name1 = Order.objects.all().filter(dept=dept, lq_date_time__contains=nian_yue,food_name__contains="盒饭1").values('number').order_by('-date_time').distinct()
    #print(name1.query)
    for it1 in name1:
        number_h1+=it1['number']
    name2 = Order.objects.all().filter(dept=dept, lq_date_time__contains=nian_yue, food_name__contains="盒饭2").values(
        'number').order_by('-date_time').distinct()
    #print(name2.query)
    for it2 in name2:
        number_h2 += it2['number']
    shuliang_list.append({'number_h1':number_h1,'number_h2':number_h2})
    return HttpResponse(json.dumps(shuliang_list,cls=CJsonEncoder))