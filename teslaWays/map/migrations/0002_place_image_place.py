# Generated by Django 4.0.4 on 2022-05-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image_place',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/img'),
        ),
    ]