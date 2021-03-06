# Generated by Django 3.1.7 on 2021-03-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nora', '0003_auto_20210320_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='color2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='color3',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(default='bnora high quality wears give you the best for every situation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='img1',
            field=models.ImageField(blank=True, upload_to='description/'),
        ),
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, upload_to='description/'),
        ),
        migrations.AddField(
            model_name='product',
            name='img3',
            field=models.ImageField(blank=True, upload_to='description/'),
        ),
        migrations.AddField(
            model_name='product',
            name='rated',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='product',
            name='ratees',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='size1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='size2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='size3',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
