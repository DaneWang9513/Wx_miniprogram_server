# Generated by Django 2.2.7 on 2019-11-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_order_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='typeName',
            field=models.CharField(default='星期一', max_length=50, verbose_name='星期'),
            preserve_default=False,
        ),
    ]
