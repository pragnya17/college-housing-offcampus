# Generated by Django 3.2.9 on 2021-11-28 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0031_delete_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='property',
        ),
    ]
