from django.db import models
from django.utils.html import format_html
# Create your models here.


class sms(models.Model):
    to_id = models.CharField(blank=True,max_length=200,verbose_name='接受者')  # 种类
    remind_flag = models.CharField(blank=True,max_length=200,verbose_name='接收标记')  # 名字
    body = models.TextField(blank=True,verbose_name='提醒内容')
    remind_time = models.IntegerField(blank=True,verbose_name='提醒时间')

    class Meta:
        verbose_name = '提醒记录'
        verbose_name_plural = '提醒记录'