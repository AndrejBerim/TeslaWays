from django.shortcuts import render, render
from django_admin_geomap import geomap_context
from . models import Place, Location


# Create your views here.


def mapIndex(request):

    return render(request, "map.html", geomap_context(Location.objects.all()))


# def getAddress(request, address):
#     address = Place.objects.get(address=address)
#     context = {
#         'address': address,
#     }
#     return render(request, 'map.html', context)
