# Generated by Django 2.2.7 on 2019-11-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_order_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='u_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='姓名'),
        ),
    ]
