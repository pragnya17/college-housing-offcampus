# Generated by Django 3.2.8 on 2021-11-08 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0013_property_parking'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='floorplan',
            field=models.ImageField(default='floorplan.jpg', upload_to='floorplans'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='parking',
            field=models.CharField(default='', max_length=20),
        ),
    ]
