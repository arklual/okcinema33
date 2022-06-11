from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
 
urlpatterns = [
    path('movie-list', views.movie_list, name='movie_list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)