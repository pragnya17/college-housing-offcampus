# Generated by Django 3.2.8 on 2021-11-14 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0017_auto_20211114_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='property_title',
            new_name='review_title',
        ),
    ]