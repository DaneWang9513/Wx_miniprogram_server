# Generated by Django 2.2.1 on 2020-03-03 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weixinlogin', '0012_auto_20200301_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_bumenzc',
            field=models.CharField(blank=True, max_length=150, verbose_name='是否具有部门资产权限'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_gerenzc',
            field=models.CharField(blank=True, max_length=150, verbose_name='是否具有个人资产权限'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_saomazc',
            field=models.CharField(blank=True, max_length=150, verbose_name='是否具有扫码资产权限'),
        ),
    ]
