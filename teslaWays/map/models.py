from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.


class Place(models.Model):
    TYPE_CHOICES = (
        ('eat', 'eat'),
        ('sleep', 'sleep'),
        ('attraction', 'attraction')
    )
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=60, null=True, blank=True)
    website = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(default="Opis")
    type_of_place = MultiSelectField(
        choices=TYPE_CHOICES, max_choices=3, max_length=20, null=True, blank=True)
    longitude = models.FloatField(default=20.468565, blank=True)
    latitude = models.FloatField(default=44.796942, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    place_region = models.ManyToManyField(
        "mainApp.Region", related_name="region_place")
    place_city = models.ManyToManyField(
        "mainApp.City", related_name="city_place")

    class Meta:
        ordering = ['-date_updated']

    def __str__(self):
        return self.name
