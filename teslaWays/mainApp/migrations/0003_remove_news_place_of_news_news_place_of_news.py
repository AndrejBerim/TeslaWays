# Generated by Django 4.0.4 on 2022-05-23 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
        ('mainApp', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='place_of_news',
        ),
        migrations.AddField(
            model_name='news',
            name='place_of_news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='map.place'),
        ),
    ]
