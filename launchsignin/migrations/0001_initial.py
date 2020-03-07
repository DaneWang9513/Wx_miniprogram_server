# Generated by Django 2.1.7 on 2019-11-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FormID', models.CharField(max_length=250, verbose_name='活动id')),
                ('startTime', models.CharField(max_length=250, verbose_name='启动时间')),
                ('endTime', models.CharField(max_length=250, verbose_name='结束时间')),
                ('FormerID', models.CharField(max_length=250, verbose_name='活动发起人id')),
                ('topic', models.CharField(max_length=250, verbose_name='签到主题')),
                ('content', models.CharField(max_length=250, verbose_name='签到内容')),
            ],
            options={
                'verbose_name': '所有签到记录',
                'verbose_name_plural': '所有签到记录',
            },
        ),
    ]
