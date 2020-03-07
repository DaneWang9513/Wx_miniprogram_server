from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser  ):
    cost = models.FloatField(default=0.0,verbose_name='用户已消费')
    dept = models.CharField(blank=True, max_length=150, verbose_name='部门')
    user_oa_id = models.CharField(blank=True, max_length=150, verbose_name='OA用户id')
    dept_id = models.CharField(blank=True, max_length=150, verbose_name='部门id')
    openid = models.CharField(max_length=100, blank=True, null=True, verbose_name="openid")
    tel_no_dept = models.CharField(max_length=100, blank=True, verbose_name="工作电话")
    mobile_no = models.CharField(max_length=100, blank=True, verbose_name="手机")
    paixu_id = models.IntegerField(blank=True,verbose_name="通讯录排序号")
    is_saomazc = models.CharField(blank=True,max_length=150,verbose_name="是否具有扫码资产权限")
    is_gerenzc = models.CharField(blank=True,max_length=150,verbose_name="是否具有个人资产权限")
    is_bumenzc = models.CharField(blank=True,max_length=150,verbose_name="是否具有部门资产权限")
    is_mes = models.CharField(blank=True,max_length=150,verbose_name="是否具有MES模块权限")
    user_mes_id = models.CharField(blank=True, max_length=150, verbose_name='MES用户id')
    user_mes_dept = models.CharField(blank=True, max_length=150, verbose_name='MES部门id')
    is_gerengz = models.CharField(blank=True, max_length=150, verbose_name="是否具有工资查询权限")

    class Meta():
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name