# Generated by Django 2.2.1 on 2020-01-11 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryMenu', '0026_auto_20191127_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='typeName',
            field=models.CharField(max_length=50, verbose_name='种类'),
        ),
    ]
