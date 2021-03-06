# Generated by Django 4.0.4 on 2022-05-27 10:24

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(blank=True, max_length=60, null=True)),
                ('website', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.TextField(default='Opis')),
                ('type_of_place', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('eat', 'eat'), ('sleep', 'sleep'), ('attraction', 'attraction')], max_length=20, null=True)),
                ('longitude', models.FloatField(blank=True, default=20.468565)),
                ('latitude', models.FloatField(blank=True, default=44.796942)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('place_city', models.ManyToManyField(related_name='city_place', to='mainApp.city')),
                ('place_region', models.ManyToManyField(related_name='region_place', to='mainApp.region')),
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
            },
        ),
    ]
