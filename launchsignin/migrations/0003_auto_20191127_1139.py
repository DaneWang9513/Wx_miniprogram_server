# Generated by Django 2.1.7 on 2019-11-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchsignin', '0002_auto_20191127_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='SigninRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FormID', models.CharField(blank=True, max_length=250, verbose_name='活动id')),
                ('studentID', models.CharField(blank=True, max_length=250, verbose_name='签到人id')),
                ('studentName', models.CharField(blank=True, max_length=250, verbose_name='签到人姓名')),
                ('topic', models.CharField(blank=True, max_length=250, verbose_name='签到主题')),
            ],
            options={
                'verbose_name': '所有签到记录',
                'verbose_name_plural': '所有签到记录',
            },
        ),
        migrations.AlterModelOptions(
            name='signin',
            options={'verbose_name': '所有发起记录', 'verbose_name_plural': '所有发起记录'},
        ),
    ]