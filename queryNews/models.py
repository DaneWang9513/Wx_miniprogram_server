from django.db import models
from django.utils.html import format_html
# Create your models here.


class news(models.Model):
    subject = models.CharField(max_length=200,verbose_name='新闻标题')  # 种类
    content = models.TextField(verbose_name='新闻内容')  # 名字
    provider = models.CharField(max_length=200,verbose_name='发布者')
    news_time = models.DateTimeField(verbose_name='发布时间')
    attachment_name = models.TextField(verbose_name='附件')
    type_id = models.CharField(max_length=200,verbose_name='新闻类型')
    to_id = models.TextField(verbose_name='发布部门')
    priv_id = models.TextField(verbose_name='发布角色')
    user_name = models.TextField(verbose_name='发布人员')
    keyword = models.CharField(blank=True,max_length=200,verbose_name='关键字')

    class Meta:
        verbose_name = '新闻记录'
        verbose_name_plural = '新闻记录'