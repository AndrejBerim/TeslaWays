# Generated by Django 4.0.4 on 2022-05-27 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainApp', '0001_initial'),
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='place_of_news',
            field=models.ManyToManyField(related_name='news_place', to='map.place'),
        ),
        migrations.AddField(
            model_name='city',
            name='city_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.country'),
        ),
        migrations.AddField(
            model_name='city',
            name='city_region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.region'),
        ),
    ]
