from django.db import models

# Create your models here.

class Order_tj(models.Model):
    lq_date_time = models.DateTimeField(blank=True, verbose_name='领取时间')
    dept = models.CharField(blank=True, max_length=150, verbose_name='部门')
    number_h1 = models.IntegerField(blank=True,default=0,verbose_name='盒饭1数量')
    number_h2 = models.IntegerField(blank=True, default=0, verbose_name='盒饭2数量')

    class Meta:
        verbose_name = '按部门订单统计'
        verbose_name_plural = '按部门订单统计'