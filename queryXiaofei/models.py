from django.db import models

# Create your models here.


class xiaofei(models.Model):
    username = models.CharField(max_length=200,verbose_name='用户名')
    wacc_sj = models.DateTimeField(verbose_name='消费时间')
    New_card_cash = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='现现金额')
    New_card_subsidy = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='现补贴额')
    Cash_amt = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='现金消费')
    Sub_amt = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='补贴消费')

    class Meta:
        verbose_name = '消费记录'
        verbose_name_plural = '消费记录'
