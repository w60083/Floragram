# Generated by Django 3.1.8 on 2021-06-24 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210620_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_of_growth_stage',
            name='plant_name',
            field=models.TextField(default='Plant'),
        ),
    ]
