# Generated by Django 3.2.9 on 2021-11-29 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0033_rating_property_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='avg_amenities',
        ),
    ]