# Generated by Django 3.2.9 on 2021-11-21 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0028_auto_20211120_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='avg_amenities',
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_title',
        ),
        migrations.AddField(
            model_name='review',
            name='property',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='property', to='housing_app.property'),
        ),
    ]
