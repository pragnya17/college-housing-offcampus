# Generated by Django 3.2.9 on 2021-12-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_remove_discussion_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='csrf',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
