# Generated by Django 3.2 on 2021-04-22 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nora', '0014_alter_desk_deliverydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='desk',
            name='deliveryAddress',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='desk',
            name='deliveryDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 10, 54, 46, 858104)),
        ),
    ]