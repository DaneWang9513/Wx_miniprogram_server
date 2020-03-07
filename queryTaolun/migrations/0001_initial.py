# Generated by Django 2.1.7 on 2019-12-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taolun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200, verbose_name='发布者id')),
                ('provider', models.CharField(max_length=200, verbose_name='发布者')),
                ('subject', models.CharField(max_length=200, verbose_name='讨论标题')),
                ('content', models.TextField(verbose_name='讨论内容')),
                ('attachment_name', models.TextField(verbose_name='附件')),
                ('submit_time', models.DateTimeField(verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '讨论记录',
                'verbose_name_plural': '讨论记录',
            },
        ),
    ]
