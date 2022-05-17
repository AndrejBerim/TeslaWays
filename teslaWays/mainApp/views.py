from django.shortcuts import render
# from geopy.geocoders import Nominatim
from mainApp.models import *
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
    regions = Region.objects.all()

    context = {
        'all_regions': regions,
    }
    return render(request, 'navbar_secondary.html', context)
