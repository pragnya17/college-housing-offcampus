# Generated by Django 3.2.8 on 2021-11-13 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing_app', '0014_auto_20211113_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('deepthought', models.TextField()),
            ],
        ),
    ]