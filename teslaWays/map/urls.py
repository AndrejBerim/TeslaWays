from django.urls import path
from . import views

urlpatterns = [
    path('', views.mapIndex, name="map_page"),
]
