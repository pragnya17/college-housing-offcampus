# Generated by Django 3.2.8 on 2021-10-31 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0010_auto_20211029_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='amentities',
            new_name='amenities',
        ),
        migrations.AddField(
            model_name='property',
            name='distance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
