from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('novosti/', views.all_news, name="news_page"),
    path('novosti/novosti/<str:pk>/', views.single_news, name='single_news'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
