# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-07 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20190507_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todayorder',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]