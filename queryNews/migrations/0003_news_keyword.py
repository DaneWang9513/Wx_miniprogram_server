# Generated by Django 2.2.1 on 2020-02-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryNews', '0002_auto_20191129_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='keyword',
            field=models.CharField(blank=True, max_length=200, verbose_name='关键字'),
        ),
    ]
