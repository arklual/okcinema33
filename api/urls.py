from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
 
urlpatterns = [
    path('film-list', views.film_list, name='film_list'),
    path('serial-list', views.serial_list, name='serial_list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)