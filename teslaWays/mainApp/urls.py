from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('novosti/', views.all_news, name="news_page"),
    path('novosti/novost/<str:pk>/', views.single_news, name='single_news'),
<<<<<<< HEAD
    path('regioni/', views.all_regions, name="regions_page"),
=======
    path('regioni/', views.all_regions, name="all_regions"),
    path("region/<str:pk>/", views.get_region, name="region_page"),
>>>>>>> andrej
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
