# Generated by Django 2.2.7 on 2019-11-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20190519_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dept',
            field=models.CharField(blank=True, max_length=150, verbose_name='部门'),
        ),
    ]