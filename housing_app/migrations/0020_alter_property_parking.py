# Generated by Django 3.2.9 on 2021-11-11 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0019_merge_0014_auto_20211107_2317_0018_auto_20211106_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='parking',
            field=models.CharField(default='No', max_length=20),
        ),
    ]
