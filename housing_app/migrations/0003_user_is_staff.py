# Generated by Django 3.2.8 on 2021-10-11 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0002_remove_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
