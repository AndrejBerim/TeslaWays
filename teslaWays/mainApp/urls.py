from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('novosti/', views.all_news, name="news_page"),
    path('novosti/novost/<str:pk>/', views.single_news, name='single_news'),
    path('regioni/', views.all_regions, name="all_regions"),
    path("region/<str:pk>/", views.get_region, name="region_page"),
    path('o_nama/', views.about_us, name="about_us_page"),
    path('map2/', views.get_address, name="map2_page")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
