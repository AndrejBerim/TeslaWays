from django.contrib import admin
from .models import Place

# Register your models here.

#Place
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'longitude','latitude','website','type_of_place',]

admin.site.register(Place, PlaceAdmin)

# admin.site.register(Place)
