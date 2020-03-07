from django.db import models

# Create your models here.
class SigninRecord(models.Model):
    FormID = models.CharField(blank=True,max_length=250, verbose_name='活动id')
    studentID = models.CharField(blank=True,max_length=250, verbose_name='签到人id')
    studentName = models.CharField(blank=True,max_length=250, verbose_name='签到人姓名')
    topic = models.CharField(blank=True,max_length=250, verbose_name='签到主题')
    #topic = models.CharField(blank=True,max_length=250, verbose_name='签到主题')
    #content = models.CharField(blank=True,max_length=250, verbose_name='签到内容')

    class Meta:
        verbose_name = '所有签到记录'
        verbose_name_plural = '所有签到记录'