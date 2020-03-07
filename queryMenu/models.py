from django.db import models
from django.utils.html import format_html
# Create your models here.


class menu(models.Model):
    typeName = models.CharField(max_length=50,verbose_name='种类')  # 种类
    name = models.CharField(max_length=50,verbose_name='名字')  # 名字
    src = models.ImageField(default='image/defaultImg.jpg', upload_to='image',verbose_name='图片')
    sales = models.IntegerField(default=0,verbose_name='可预订数量')
    sales_fz = models.IntegerField(default=0, verbose_name='阈值')
    rating = models.FloatField(default=5,verbose_name='评分')
    price = models.FloatField(default=0.0,verbose_name='售价')
    status_type = (('上架', u'上架'), ('下架', u'下架'))
    status = models.CharField(default='下架',verbose_name='是否上架',max_length=30,choices=status_type)
    xiaoliang = models.IntegerField(default=0, verbose_name='销量')
    jz_date_time = models.DateTimeField(verbose_name='截止时间')
    lq_date_time = models.DateTimeField(verbose_name='领取时间')
    fh_type = (('符合', u'符合'), ('不符合', u'不符合'))
    fh_status = models.CharField(default='不符合', verbose_name='是否符合出售', max_length=30, choices=fh_type)

    def image_data(self):
        if self.src.url:
            return format_html(
            '<img src="{}" width="100px" />',
            self.src.url,
            )

    image_data.short_description = u'图片'

    class Meta:
        verbose_name = '预订餐品'
        verbose_name_plural = '预订餐品'