# Generated by Django 5.0.3 on 2024-07-23 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0022_alter_comments_upload_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 23, 22, 34, 52, 306230)),
        ),
    ]
