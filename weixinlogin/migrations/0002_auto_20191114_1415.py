# Generated by Django 2.2.7 on 2019-11-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weixinlogin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]