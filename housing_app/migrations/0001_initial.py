<<<<<<< HEAD
# Generated by Django 3.2.9 on 2021-11-14 08:19
=======
# Generated by Django 3.2.8 on 2021-10-11 03:52
>>>>>>> 81454e456d9655f3dba7a791f1d9571258ad734e

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=75)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('distance', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('furnished', models.CharField(default='No', max_length=3)),
                ('parking', models.CharField(default='No', max_length=20)),
                ('bedrooms', models.IntegerField(default=1)),
                ('bathrooms', models.IntegerField(default=1)),
                ('address', models.CharField(max_length=200)),
                ('services', models.TextField(default='')),
                ('amenities', models.TextField(default='')),
                ('favorite', models.BooleanField(default=False)),
                ('floorplan', models.ImageField(upload_to='floorplans')),
                ('picture', models.ImageField(default='', upload_to='pictures')),
            ],
            options={
                'verbose_name_plural': 'properties',
            },
        ),
        migrations.CreateModel(
=======
>>>>>>> 81454e456d9655f3dba7a791f1d9571258ad734e
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
