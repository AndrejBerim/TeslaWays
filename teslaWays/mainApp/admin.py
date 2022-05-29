from django.contrib import admin
from .models import *

# Register your models here.

# About Us
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']

admin.site.register(AboutUs, AboutUsAdmin)

#News
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'news_image']

admin.site.register(News, NewsAdmin)

#Region
class RegionAdmin(admin.ModelAdmin):
    list_display = ['region_name', 'date_created', 'region_country']

admin.site.register(Region, RegionAdmin)

#City
class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name','city_region', 'date_created', 'city_country']

admin.site.register(City, CityAdmin)

admin.site.register(Country)

admin.site.register(Member)
