# Generated by Django 2.2.1 on 2020-01-11 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryXiaofei', '0003_auto_20200111_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xiaofei',
            name='Cash_amt',
            field=models.TextField(verbose_name='现金消费'),
        ),
        migrations.AlterField(
            model_name='xiaofei',
            name='New_card_cash',
            field=models.TextField(verbose_name='现现金额'),
        ),
        migrations.AlterField(
            model_name='xiaofei',
            name='New_card_subsidy',
            field=models.TextField(verbose_name='现补贴额'),
        ),
        migrations.AlterField(
            model_name='xiaofei',
            name='Sub_amt',
            field=models.TextField(verbose_name='补贴消费'),
        ),
    ]