# Generated by Django 2.1.7 on 2019-11-29 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryNotify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifys',
            name='begin_date',
            field=models.IntegerField(verbose_name='开始时间戳'),
        ),
        migrations.AlterField(
            model_name='notifys',
            name='end_date',
            field=models.IntegerField(verbose_name='结束时间戳'),
        ),
    ]
