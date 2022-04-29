from django.shortcuts import render
from .models import *
# Create your views here.


def main_page(request):
    context = {}
<<<<<<< HEAD
    return render(request, 'pocetna.html', context)
=======
    return render(request, 'main.html', context)


def all_news(request):
    all_news = News.objects.all()

    context = {
        'all_news': all_news,

    }
    return render(request, 'novosti.html', context)
>>>>>>> 6b72777ce403536020efcfae117794c90bb374b0
