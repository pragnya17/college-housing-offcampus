# Generated by Django 3.2.9 on 2021-12-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20211202_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='discuss',
            field=models.TextField(max_length=1000),
        ),
    ]