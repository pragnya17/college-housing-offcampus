# Generated by Django 3.2.9 on 2021-12-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_remove_discussion_csrf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
