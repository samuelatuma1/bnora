# Generated by Django 3.2 on 2021-04-22 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nora', '0016_auto_20210422_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='desk',
            old_name='summarized',
            new_name='order_placed',
        ),
        migrations.AlterField(
            model_name='desk',
            name='deliveryDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 11, 58, 32, 997890)),
        ),
    ]
