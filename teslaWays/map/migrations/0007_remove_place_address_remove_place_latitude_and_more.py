# Generated by Django 4.0.4 on 2022-05-31 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_place_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='address',
        ),
        migrations.RemoveField(
            model_name='place',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='place',
            name='longitude',
        ),
    ]
