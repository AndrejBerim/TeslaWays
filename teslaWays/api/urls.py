from django.urls import path
from . import views

urlpatterns = [
    path('mesta/', views.getPlaceData),
    path('novosti/', views.getNewsData),
    path('zemlja/', views.getCountryData),
    path('regioni/', views.getRegionData),
    path('grad/', views.getCityData),
]
