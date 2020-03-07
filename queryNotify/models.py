from django.db import models
from django.utils.html import format_html
# Create your models here.


class notifys(models.Model):
    from_name = models.CharField(max_length=200,verbose_name='发布者')
    to_id = models.TextField(verbose_name='发布部门')
    subject = models.CharField(max_length=200,verbose_name='公告标题')  # 种类
    content = models.TextField(verbose_name='公告内容')  # 名字
    #provider = models.CharField(max_length=200,verbose_name='发布者')
    send_time = models.DateTimeField(verbose_name='发布时间')
    begin_date = models.IntegerField(verbose_name='开始时间戳')
    end_date = models.IntegerField(verbose_name='结束时间戳')
    attachment_name = models.TextField(verbose_name='附件')
    priv_id = models.TextField(verbose_name='发布角色')
    user_name = models.TextField(verbose_name='发布人员')
    type_id = models.CharField(max_length=200, verbose_name='公告类型')
    keyword = models.CharField(blank=True,max_length=200,verbose_name='关键字')

    class Meta:
        verbose_name = '公告记录'
        verbose_name_plural = '公告记录'