# Generated by Django 3.2 on 2021-04-22 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nora', '0013_auto_20210422_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desk',
            name='deliveryDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 6, 27, 42, 549372)),
        ),
    ]
