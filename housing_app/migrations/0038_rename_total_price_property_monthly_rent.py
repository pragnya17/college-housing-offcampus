# Generated by Django 3.2.9 on 2021-12-03 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0037_merge_20211202_2300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='total_price',
            new_name='monthly_rent',
        ),
    ]