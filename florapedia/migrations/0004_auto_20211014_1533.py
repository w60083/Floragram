# Generated by Django 3.1.8 on 2021-10-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('florapedia', '0003_auto_20211014_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='subcategory',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='plant',
            name='сategory',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
