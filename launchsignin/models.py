from django.db import models

# Create your models here.

class Signin(models.Model):
    FormID = models.CharField(blank=True,max_length=250, verbose_name='活动id')
    startTime = models.CharField(blank=True,max_length=250, verbose_name='启动时间')
    endTime = models.CharField(blank=True,max_length=250, verbose_name='结束时间')
    FormerID = models.CharField(blank=True,max_length=250, verbose_name='活动发起人id')
    topic = models.CharField(blank=True,max_length=250, verbose_name='签到主题')
    content = models.CharField(blank=True,max_length=250, verbose_name='签到内容')

    class Meta:
        verbose_name = '所有发起记录'
        verbose_name_plural = '所有发起记录'