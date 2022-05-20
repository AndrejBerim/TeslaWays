from rest_framework.response import Response
from rest_framework.decorators import api_view
from map.models import Place
from mainApp.models import (News,
                            Country,
                            Region,
                            City)
from .serializers import (PlaceSerializer,
                          NewsSerializer,
                          CountrySerializer,
                          RegionSerializer,
                          CitySerializer)


@api_view(['GET'])
def getPlaceData(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNewsData(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCountryData(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRegionData(request):
    regions = Region.objects.all()
    serializer = RegionSerializer(regions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCityData(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)
