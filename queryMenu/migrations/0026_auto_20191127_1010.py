# Generated by Django 2.1.7 on 2019-11-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryMenu', '0025_auto_20191121_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='lq_date_time',
            field=models.DateTimeField(default='2019-11-21 08:55:00.000000', verbose_name='领取时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='售价'),
        ),
    ]
