# Generated by Django 2.1.7 on 2019-11-21 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queryMenu', '0024_auto_20191121_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='xg_num',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='xg_status',
        ),
    ]