# Generated by Django 3.2 on 2021-04-22 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nora', '0015_auto_20210422_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='desk',
            name='summarized',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='desk',
            name='deliveryDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 11, 57, 16, 12278)),
        ),
    ]
