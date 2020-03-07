from django.db import models

# Create your models here.


class kaoqin(models.Model):
    username = models.CharField(max_length=200,verbose_name='用户名')
    kq_sj = models.DateTimeField(verbose_name='考勤时间')

    class Meta:
        verbose_name = '考勤记录'
        verbose_name_plural = '考勤记录'
