from django.contrib import admin
from django_admin_geomap import ModelAdmin
from . models import Place, Location

# Register your models here.

# Place


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'longitude',
                    'latitude', 'website', 'type_of_place', ]


admin.site.register(Place, PlaceAdmin)


class Admin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_default_longitude = "44.3"
    geomap_default_latitude = "20.4"
    geomap_item_zoom = "10"
    geomap_hright = "300px"


admin.site.register(Location, Admin)
