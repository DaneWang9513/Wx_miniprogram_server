# Generated by Django 2.2.7 on 2019-11-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryMenu', '0009_auto_20191118_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='sales',
            field=models.IntegerField(default=0, verbose_name='数量'),
        ),
    ]
