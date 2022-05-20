from django.shortcuts import render
# from geopy.geocoders import Nominatim
from .models import *
from map.models import Place
# Create your views here.


def main_page(request):
    context = {}
    return render(request, 'pocetna.html', context)


def about_us(request):
    context = {}
    return render(request, 'o_nama.html', context)


def all_news(request):
    all_news = News.objects.all()

    context = {
        'all_news': all_news,
    }
    return render(request, 'novosti.html', context)


def single_news(request, pk):
    novost = News.objects.get(id=pk)

    context = {
        'novost': novost,
    }
    return render(request, 'novost.html', context)


def countries(request):
    countries = Country.objects.all().values()
    print(countries)

    context = {
        'countries': countries,
    }
    return render(request, 'navbar_secondary.html', context)


def all_regions(request):
    all_region = Region.objects.all().values()

    context = {
        'all_region': all_region,
    }
    return render(request, 'all_regions.html', context)


def get_region(request, pk):
    region = Region.objects.get(id=pk)
    context = {
        'region': region,
    }
    return render(request, "all_regions.html", context)
