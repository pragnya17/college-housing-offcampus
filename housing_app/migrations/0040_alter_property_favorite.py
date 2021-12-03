# Generated by Django 3.2.9 on 2021-12-03 04:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0039_alter_property_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='fav_properties', to=settings.AUTH_USER_MODEL),
        ),
    ]