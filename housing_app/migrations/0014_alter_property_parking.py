# Generated by Django 3.2.8 on 2021-11-06 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0013_property_parking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='parking',
            field=models.CharField(default='', max_length=20),
        ),
    ]