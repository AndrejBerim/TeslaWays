# Generated by Django 4.0.4 on 2022-04-29 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_rename_place_news_news_place_of_news_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['-date_updated']},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date_updated']},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['-date_updated']},
        ),
        migrations.AlterField(
            model_name='news',
            name='place_of_news',
            field=models.ManyToManyField(blank=True, to='mainApp.place'),
        ),
    ]
