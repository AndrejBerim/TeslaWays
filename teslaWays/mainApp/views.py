from django.shortcuts import render
from . models import News
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
    single_news = News.objects.get(id=pk)
    context = {
        'single_news': single_news,
    }
    return render(request, 'novost.html', context)
