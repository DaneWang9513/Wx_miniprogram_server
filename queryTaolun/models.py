from django.db import models
from django.utils.html import format_html
# Create your models here.


class taolun(models.Model):
    user_id = models.CharField(max_length=200, verbose_name='发布者id')
    provider = models.CharField(max_length=200, verbose_name='发布者')
    subject = models.CharField(max_length=200,verbose_name='讨论标题')  # 种类
    content = models.TextField(verbose_name='讨论内容')  # 名字
    attachment_name = models.TextField(verbose_name='附件')
    submit_time = models.DateTimeField(verbose_name='发布时间')
    #type_id = models.CharField(max_length=200,verbose_name='新闻类型')
    #to_id = models.TextField(verbose_name='发布部门')
    #priv_id = models.TextField(verbose_name='发布角色')
    #user_name = models.TextField(verbose_name='发布人员')

    class Meta:
        verbose_name = '讨论记录'
        verbose_name_plural = '讨论记录'