# Generated by Django 5.0.3 on 2024-07-16 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0009_alter_comments_upload_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 16, 15, 12, 8, 789886)),
        ),
    ]
