# Generated by Django 4.0.4 on 2022-05-31 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_location_lat_location_lon_location_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='address',
        ),
    ]