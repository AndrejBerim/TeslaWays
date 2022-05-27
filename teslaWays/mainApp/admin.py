from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Member)
admin.site.register(News)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Country)
# admin.site.register(AboutUs)
# admin.site.register(Image)


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']


admin.site.register(AboutUs, AboutUsAdmin)
