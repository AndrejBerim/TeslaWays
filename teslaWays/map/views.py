from django.shortcuts import render

# Create your views here.


def mapIndex(request):

    context = {

    }
    return render(request, "map.html", context),
