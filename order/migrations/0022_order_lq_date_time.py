# Generated by Django 2.1.7 on 2019-11-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_auto_20191121_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='lq_date_time',
            field=models.DateTimeField(default='2019-11-21 08:55:00.000000', verbose_name='领取时间'),
            preserve_default=False,
        ),
    ]
