# Generated by Django 2.1.7 on 2019-11-29 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queryNews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='ATTACHMENT_NAME',
            new_name='attachment_name',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='CONTENT',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='NEWS_TIME',
            new_name='news_time',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='PRIV_ID',
            new_name='priv_id',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='PROVIDER',
            new_name='provider',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='SUBJECT',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='TO_ID',
            new_name='to_id',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='TYPE_ID',
            new_name='type_id',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='USER_ID',
            new_name='user_name',
        ),
    ]