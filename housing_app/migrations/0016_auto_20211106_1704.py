# Generated by Django 3.2.9 on 2021-11-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0015_alter_property_rooms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='rooms',
            new_name='bedrooms',
        ),
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(default=1),
        ),
    ]
