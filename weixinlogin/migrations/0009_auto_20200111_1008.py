# Generated by Django 2.2.1 on 2020-01-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weixinlogin', '0008_userprofile_openid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='openid',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='openid'),
        ),
    ]
