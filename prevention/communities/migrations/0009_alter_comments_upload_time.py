# Generated by Django 5.0.3 on 2024-07-15 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0008_comments_likes_reply_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 21, 12, 2, 333977)),
        ),
    ]
