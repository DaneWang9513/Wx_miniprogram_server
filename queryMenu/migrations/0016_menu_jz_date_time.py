# Generated by Django 2.1.7 on 2019-11-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryMenu', '0015_menu_xiaoliang'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='jz_date_time',
            field=models.DateTimeField(default='2019-11-16 20:20:16.000000', verbose_name='截止时间'),
            preserve_default=False,
        ),
    ]
