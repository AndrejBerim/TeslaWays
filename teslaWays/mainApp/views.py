from django.shortcuts import render, redirect
from map.models import Place, Location
import geocoder
import folium
from django.http import HttpResponse
from . models import *

# Create your views here.


def main_page(request):
    all_region = Region.objects.all()
    context = {
        'all_region': all_region,
    }
    return render(request, 'pocetna.html', context)


def all_news(request):
    all_news = News.objects.all()
    all_region = Region.objects.all()
    context = {
        'all_news': all_news,
        'all_region': all_region,
    }
    return render(request, 'novosti.html', context)


def single_news(request, pk):
    novost = News.objects.get(id=pk)
    all_region = Region.objects.all()
    context = {
        'novost': novost,
        'all_region': all_region,
    }
    return render(request, 'novost.html', context)


def countries(request):
    countries = Country.objects.all().values()
    context = {
        'countries': countries,
    }
    return render(request, 'navbar_secondary.html', context)


def all_regions(request):
    all_region = Region.objects.all()
    context = {
        'all_region': all_region,
    }
    return render(request, 'navbar_secondary.html', context)


def get_region(request, pk):
    region = Region.objects.get(id=pk)
    context = {
        'region': region,
    }
    return render(request, "all_regions.html", context)


def about_us(request):
    info_data = AboutUs.objects.all()
    all_region = Region.objects.all()
    context = {
        'info_data': info_data,
        'all_region': all_region,
    }
    return render(request, 'o_nama.html', context)


def get_address(request):
    address = Location.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    print(f"Longitude: {lng} - Latitude: {lat} <--> {country}")
    if (lat == None) or (lng == None):
        address.delete()
        return HttpResponse('Address is not valid!')

    # Create map object
    mapObj = folium.Map(location=[44.787197, 20.457273], zoom_start=8)
    folium.Marker([lat, lng], tooltip="Click for more info",
                  popup=f"Wecome to {address}").add_to(mapObj)

    # Get HTML Representation of Map Object
    mapObj = mapObj._repr_html_()
    return render(request, 'map2.html', {
        'mapObj': mapObj,
    })
