# Generated by Django 3.2.9 on 2021-12-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_alter_discussion_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myforum',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
