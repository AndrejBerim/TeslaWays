from django.shortcuts import render
from .models import *
# Create your views here.


def main_page(request):
    context = {}
    return render(request, 'main.html', context)


def all_news(request):
    all_news = News.objects.all()

    context = {
        'all_news': all_news,

    }
    return render(request, 'novosti.html', context)
