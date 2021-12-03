# Generated by Django 3.2.9 on 2021-12-03 04:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0037_merge_20211202_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='favorite',
            field=models.ManyToManyField(related_name='fav_properties', to=settings.AUTH_USER_MODEL),
        ),
    ]
