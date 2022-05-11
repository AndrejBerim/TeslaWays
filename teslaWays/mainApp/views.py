from django.shortcuts import render
from . models import News, Region, City, Place
# Create your views here.


def main_page(request):
    context = {}
    return render(request, 'pocetna.html', context)


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


def all_regions(request):
    regions = Region.objects.all()

    context = {
        'regions': regions,
    }
    return render(request, 'navbar_primary.html', context)
