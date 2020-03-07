# Generated by Django 2.2.1 on 2020-03-01 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_id', models.CharField(blank=True, max_length=200, verbose_name='接受者')),
                ('remind_flag', models.CharField(blank=True, max_length=200, verbose_name='接收标记')),
                ('body', models.TextField(blank=True, verbose_name='提醒内容')),
                ('remind_time', models.IntegerField(blank=True, max_length=11, verbose_name='提醒时间')),
            ],
            options={
                'verbose_name': '提醒记录',
                'verbose_name_plural': '提醒记录',
            },
        ),
    ]