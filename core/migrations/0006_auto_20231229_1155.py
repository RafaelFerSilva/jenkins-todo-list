# Generated by Django 2.1.7 on 2023-12-29 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190325_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 29, 11, 55, 44, 341159)),
        ),
    ]
