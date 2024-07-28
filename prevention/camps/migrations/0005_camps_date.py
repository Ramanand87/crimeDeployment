# Generated by Django 5.0.3 on 2024-07-24 09:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0004_remove_camps_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='camps',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]