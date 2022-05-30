from django.db import models
from multiselectfield import MultiSelectField
from django_admin_geomap import GeoItem
from mainApp.models import *


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
    image_place = models.ImageField(
        upload_to='staticfiles/img', null=True, blank=True)
    type_of_place = MultiSelectField(
        choices=TYPE_CHOICES, max_choices=3, max_length=20, null=True, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    place_region = models.ManyToManyField(
        Region, related_name="region_place")
    place_city = models.ManyToManyField(
        City, related_name="city_place")

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"

    def __str__(self):
        return self.name


class Location(models.Model, GeoItem):
    name = models.CharField(max_length=100, null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)  # longitude
    lat = models.FloatField(null=True, blank=True)  # latitude

    def __str__(self):
        return str(self.name)

    @property
    def geomap_longitude(self):
        return '' if self.lon == None else str(self.lon)

    @property
    def geomap_latitude(self):
        return '' if self.lat == None else str(self.lat)

    @property
    def geomap_icon(self):
        return self.default_icon

    @property
    def geomap_popup_view(self):
        return "<strong>{}</strong>".format(str(self))

    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view

    @property
    def geomap_popup_common(self):
        return self.geomap_popup_view
