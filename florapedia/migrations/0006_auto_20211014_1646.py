# Generated by Django 3.1.8 on 2021-10-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('florapedia', '0005_auto_20211014_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='plant',
            name='subcategory',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
