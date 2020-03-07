from django.db import models

# Create your models here.


class Order(models.Model):
    username = models.CharField(blank=True,max_length=200,verbose_name='用户名')
    order_id = models.CharField(blank=True,max_length=200,verbose_name='订单号')
    food_name = models.CharField(blank=True,max_length=50,verbose_name='名字')
    comment = models.CharField(blank=True,max_length=200,verbose_name='评论')
    score = models.IntegerField(blank=True,default=5,verbose_name='评分')
    date_time = models.DateTimeField(blank=True,verbose_name='下单时间')
    number = models.IntegerField(blank=True,default=0,verbose_name='数量')
    state = models.CharField(blank=True,max_length=20,verbose_name='订单状态')
    cost = models.FloatField(blank=True,default=9999.0,verbose_name='订单总价')
    dept = models.CharField(blank=True, max_length=150, verbose_name='部门')
    first_name = models.CharField(blank=True, max_length=150, verbose_name='姓名')
    typeName = models.CharField(blank=True,max_length=50, verbose_name='种类')
    jz_date_time = models.DateTimeField(blank=True,verbose_name='截止时间')
    lq_date_time = models.DateTimeField(blank=True,verbose_name='领取时间')

    class Meta:
        verbose_name = '所有订单'
        verbose_name_plural = '所有订单'


class TodayOrder(models.Model):
    date_time = models.DateTimeField(verbose_name='时间')
    food_name = models.CharField(max_length=50,verbose_name='名字')
    number = models.IntegerField(default=0,verbose_name='数量')
    state = models.CharField(max_length=20,default='未完成',verbose_name='状态')

    class Meta:
        verbose_name = '每日订单汇总'
        verbose_name_plural = '每日订单汇总'